import pytest
from sqlalchemy import create_engine, text


DB_USER = "postgres"      # Имя пользователя
DB_PASSWORD = "123"       # Пароль
DB_HOST = "localhost"     # Адрес хоста
DB_PORT = "5432"          # Порт
DB_NAME = "postgres"      # Имя базы данных

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False)


# Вспомогательные функции

def create_subject(title):
    """
    Создает новый предмет в таблице subject

    Структура таблицы subject:
    - subject_id: INTEGER (первичный ключ)
    - subject_title: VARCHAR NOT NULL
    """
    with engine.connect() as connection:
        with connection.begin():
            # Находим максимальный ID, чтобы добавить новый
            max_id_result = connection.execute(text(
                "SELECT COALESCE(MAX(subject_id), 0) FROM subject"))
            max_id = max_id_result.scalar()
            new_id = max_id + 1

            # Вставляем новый предмет
            sql = text("""
                INSERT INTO subject (subject_id, subject_title)
                VALUES (:new_id, :title)
            """)
            connection.execute(sql, {"new_id": new_id, "title": title})
            return new_id


def get_subject_by_id(subject_id):
    """
    Получает предмет по ID
    """
    with engine.connect() as connection:
        sql = text("SELECT * FROM subject WHERE subject_id = :subject_id")
        result = connection.execute(sql, {"subject_id": subject_id})
        row = result.fetchone()

        if row:
            return dict(row._mapping)
        return None


def delete_subject(subject_id):
    """
    Физически удаляет предмет из БД (для очистки)
    """
    with engine.connect() as connection:
        with connection.begin():
            sql = text("DELETE FROM subject WHERE subject_id = :subject_id")
            connection.execute(sql, {"subject_id": subject_id})


def subject_exists(subject_id):
    """
    Проверяет, существует ли предмет в БД
    """
    return get_subject_by_id(subject_id) is not None


def test_add_new_subject():
    """
    ТЕСТ: Добавление нового предмета
    """
    print("\n" + "="*60)
    print("ТЕСТ: ДОБАВЛЕНИЕ НОВОГО ПРЕДМЕТА")
    print("="*60)

    # 1. ПОДГОТОВКА ТЕСТОВЫХ ДАННЫХ
    test_title = "Программирование на Python"
    print(f"📝 Название предмета: {test_title}")

    subject_id = None

    try:
        # 2. ВЫПОЛНЕНИЕ ОПЕРАЦИИ ДОБАВЛЕНИЯ
        print("\n➡ Выполняем INSERT в таблицу subject...")
        subject_id = create_subject(test_title)
        print(f"✓ Предмет создан с ID: {subject_id}")

        # 3. ПРОВЕРКА РЕЗУЛЬТАТА
        print("\n➡ Проверяем, что данные сохранились...")
        created_subject = get_subject_by_id(subject_id)

        # Ассерт 1: предмет должен существовать
        assert created_subject is not None, "Предмет не найден в БД"
        print("✓ Предмет найден в базе данных")

        # Ассерт 2: ID должен совпадать
        assert created_subject["subject_id"] == subject_id, \
            "ID не совпадает"
        print(f"ID совпадает: {created_subject['subject_id']}")

        # Ассерт 3: название должно совпадать
        assert created_subject["subject_title"] == test_title, \
            "Название не совпадает"
        print(f"Название совпадает: {created_subject['subject_title']}")

        print("\n" + "🎉" * 10)
        print("ТЕСТ УСПЕШНО ПРОЙДЕН! Предмет добавлен.")
        print("🎉" * 10)

    except AssertionError as e:
        print(f"\n Ошибка проверки: {e}")
        raise
    except Exception as e:
        print(f"\n Непредвиденная ошибка: {e}")
        raise
    finally:
        # 4. ОЧИСТКА
        if subject_id:
            print(f"\n Очистка: удаляем предмет с ID {subject_id}")
            delete_subject(subject_id)
            if not subject_exists(subject_id):
                print("Тестовый предмет удален из БД")
            else:
                print("Не удалось удалить предмет")
        print("="*60 + "\n")


def test_connection():
    """
    Проверка подключения к БД и структуры таблицы subject
    """
    print("\n Проверка подключения...")
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.fetchone()[0] == 1
            print("✓ Подключение к БД успешно!")

            # Проверяем таблицу subject
            from sqlalchemy import inspect
            inspector = inspect(engine)
            tables = inspector.get_table_names()

            if "subject" in tables:
                print("Таблица 'subject' существует")

                # Проверяем структуру таблицы
                columns = inspector.get_columns("subject")
                column_names = [col["name"] for col in columns]
                print(f"Колонки в таблице subject: {column_names}")

                # Проверяем наличие нужных колонок
                assert "subject_id" in column_names, "Нет колонки subject_id"
                assert "subject_title" in column_names, "Нет колонки subject_title"
                print("Структура таблицы корректна")
            else:
                print("Таблица 'subject' не найдена!")

    except Exception as e:
        print(f"Ошибка: {e}")
        assert False, "Не удалось подключиться к БД"
    print("="*60 + "\n")


if __name__ == "__main__":
    test_connection()
    pytest.main([__file__, "-v", "-s"])
