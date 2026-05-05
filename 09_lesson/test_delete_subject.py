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
    Создает тестовый предмет для последующего удаления
    """
    with engine.connect() as connection:
        with connection.begin():
            max_id_result = connection.execute(text(
                "SELECT COALESCE(MAX(subject_id), 0) FROM subject"))
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


def delete_subject(subject_id):
    """
    Удаляет предмет из БД (физическое удаление)
    """
    with engine.connect() as connection:
        with connection.begin():
            sql = text("DELETE FROM subject WHERE subject_id = :subject_id")
            result = connection.execute(sql, {"subject_id": subject_id})
            return result.rowcount


def subject_exists(subject_id):
    """Проверяет существование предмета"""
    return get_subject_by_id(subject_id) is not None


def test_delete_subject():
    """
    ТЕСТ: Удаление предмета
    """
    print("\n" + "="*60)
    print("ТЕСТ: УДАЛЕНИЕ ПРЕДМЕТА")
    print("="*60)

    # 1. ПОДГОТОВКА: создаем предмет
    test_title = "Предмет для удаления"
    print(f"Название предмета: {test_title}")

    subject_id = None

    try:
        subject_id = create_test_subject(test_title)
        print(f"Создан предмет с ID: {subject_id}")

        # Проверяем, что предмет существует
        assert subject_exists(subject_id), "Предмет не был создан"
        print("Предмет существует перед удалением")

        # 2. ВЫПОЛНЕНИЕ ОПЕРАЦИИ УДАЛЕНИЯ
        print("\n Выполняем DELETE из таблицы subject...")
        rows_deleted = delete_subject(subject_id)
        print(f" Удалено строк: {rows_deleted}")

        # 3. ПРОВЕРКА РЕЗУЛЬТАТА
        print("\n Проверяем, что предмет удален...")

        # Ассерт 1: должна быть удалена 1 строка
        assert rows_deleted == 1, \
            f"Удалено {rows_deleted} строк, ожидалось 1"
        print("Удалена ровно 1 строка")

        # Ассерт 2: предмет не должен существовать в БД
        assert not subject_exists(subject_id), \
            "Предмет все еще существует в БД после удаления!"
        print("✓ Предмет больше не найден в базе данных")

        print("\n" + "🎉" * 10)
        print("ТЕСТ УСПЕШНО ПРОЙДЕН! Предмет удален.")
        print("🎉" * 10)

        # Очистка не нужна, так как предмет уже удален
        subject_id = None

    except AssertionError as e:
        print(f"\n Ошибка проверки: {e}")
        raise
    except Exception as e:
        print(f"\n Непредвиденная ошибка: {e}")
        raise
    finally:
        # 4. ОЧИСТКА НА ВСЯКИЙ СЛУЧАЙ (если тест упал до удаления)
        if subject_id and subject_exists(subject_id):
            print(f"\n Очистка: удаляем предмет с ID {subject_id}")
            delete_subject(subject_id)
            print("✓ Тестовый предмет удален")
        print("="*60 + "\n")


def test_delete_nonexistent_subject():
    """
    ДОПОЛНИТЕЛЬНЫЙ ТЕСТ: Попытка удалить несуществующий предмет
    Проверяет, что удаление несуществующей записи возвращает 0
    """
    print("\n" + "="*60)
    print("ДОП. ТЕСТ: УДАЛЕНИЕ НЕСУЩЕСТВУЮЩЕГО ПРЕДМЕТА")
    print("="*60)

    # Используем заведомо несуществующий ID
    nonexistent_id = 999999

    try:
        rows_deleted = delete_subject(nonexistent_id)

        # Ассерт: должно быть удалено 0 строк
        assert rows_deleted == 0, \
            f"При удалении несуществующего ID удалено {rows_deleted} строк"
        print("Удаление несуществующего предмета вернуло 0")

        print("\n Дополнительный тест пройден!")

    except AssertionError as e:
        print(f"\nОшибка: {e}")
        raise
    print("="*60 + "\n")


def test_connection():
    """Проверка подключения"""
    print("\n Проверка подключения...")
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.fetchone()[0] == 1
            print("✓ Подключение к БД успешно!")
    except Exception as e:
        print(f"Ошибка: {e}")
        assert False
    print("="*60 + "\n")


if __name__ == "__main__":
    test_connection()
    pytest.main([__file__, "-v", "-s"])
