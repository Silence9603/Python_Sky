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

def create_test_subject(title):
    """
    Создает тестовый предмет для последующего изменения
    """
    with engine.connect() as connection:
        with connection.begin():
            max_id_result = connection.execute(
                text("SELECT COALESCE(MAX(subject_id), 0) FROM subject"))
            max_id = max_id_result.scalar()
            new_id = max_id + 1

            sql = text("INSERT INTO subject (subject_id, subject_title) VALUES (:new_id, :title)")
            connection.execute(sql, {"new_id": new_id, "title": title})
            return new_id


def get_subject_by_id(subject_id):
    """Получает предмет по ID"""
    with engine.connect() as connection:
        sql = text("SELECT * FROM subject WHERE subject_id = :subject_id")
        result = connection.execute(sql, {"subject_id": subject_id})
        row = result.fetchone()
        if row:
            return dict(row._mapping)
        return None


def update_subject_title(subject_id, new_title):
    """
    Обновляет название предмета
    Возвращает количество обновленных строк
    """
    with engine.connect() as connection:
        with connection.begin():
            sql = text("""
                UPDATE subject
                SET subject_title = :new_title
                WHERE subject_id = :subject_id
            """)
            result = connection.execute(sql, {
                "new_title": new_title,
                "subject_id": subject_id
            })
            return result.rowcount


def delete_subject(subject_id):
    """Удаляет предмет"""
    with engine.connect() as connection:
        with connection.begin():
            sql = text("DELETE FROM subject WHERE subject_id = :subject_id")
            connection.execute(sql, {"subject_id": subject_id})


def test_update_subject():
    """
    ТЕСТ: Изменение названия предмета
    """
    print("\n" + "="*60)
    print("ТЕСТ: ИЗМЕНЕНИЕ ПРЕДМЕТА")
    print("="*60)

    # 1. ПОДГОТОВКА: создаем предмет
    original_title = "Старое название"
    print(f"Исходное название: {original_title}")

    subject_id = None

    try:
        subject_id = create_test_subject(original_title)
        print(f" Создан предмет с ID: {subject_id}")

        # Проверяем, что создалось правильно
        before_update = get_subject_by_id(subject_id)
        assert before_update["subject_title"] == original_title
        print(f"Данные до изменения: {before_update['subject_title']}")

        # 2. ВЫПОЛНЕНИЕ ОПЕРАЦИИ ИЗМЕНЕНИЯ
        print("\n Изменяем название предмета...")
        new_title = "Новое название по SQL"
        rows_updated = update_subject_title(subject_id, new_title)
        print(f"Обновлено строк: {rows_updated}")

        # 3. ПРОВЕРКА РЕЗУЛЬТАТА
        print("\n Проверяем, что данные изменились...")
        after_update = get_subject_by_id(subject_id)

        # Ассерт 1: должна быть обновлена 1 строка
        assert rows_updated == 1, \
            f"Обновлено {rows_updated} строк, ожидалось 1"
        print("Обновлена ровно 1 строка")

        # Ассерт 2: название должно измениться
        assert after_update["subject_title"] == new_title, \
            f"Ожидалось: {new_title}, Получено: {after_update['subject_title']}"
        print(f"Название успешно изменено на: {after_update['subject_title']}")

        # Ассерт 3: ID не должен измениться
        assert after_update["subject_id"] == subject_id, \
            "ID предмета не должен был измениться"
        print(f"ID остался прежним: {after_update['subject_id']}")

        print("\n" + "🎉" * 10)
        print("ТЕСТ УСПЕШНО ПРОЙДЕН! Предмет изменен.")
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
            print("Тестовый предмет удален")
        print("="*60 + "\n")


def test_connection():
    """Проверка подключения"""
    print("\n Проверка подключения...")
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.fetchone()[0] == 1
            print("Подключение к БД успешно!")
    except Exception as e:
        print(f"Ошибка: {e}")
        assert False
    print("="*60 + "\n")


if __name__ == "__main__":
    test_connection()
    pytest.main([__file__, "-v", "-s"])
