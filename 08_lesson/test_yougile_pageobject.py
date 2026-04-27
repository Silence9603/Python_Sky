from YougileApi import YougileApi

# Инициализация API
api = YougileApi("https://yougile.com/api-v2", "ВАШ_КЛЮЧ_ДОСТУПА")

# ========== ТЕСТЫ ДЛЯ POST /projects ==========


def test_create_project_positive():
    """Позитивный тест создания проекта"""
    print("\n Тест: создание проекта")

    # Создаем проект
    result = api.create_project("PageObject тест")

    # Проверяем, что id есть и он не пустой
    assert "id" in result, "Ответ не содержит id проекта"
    project_id = result["id"]
    assert project_id is not None

    # Дополнительно проверяем, что проект создался с правильным названием
    project = api.get_project(project_id)
    assert project["title"] == "PageObject тест"

    # Очистка
    api.delete_project(project_id)
    print("Тест пройден")


def test_create_project_negative_empty_title():
    """Негативный тест: пустое название"""
    print("\n Тест: создание с пустым названием")

    resp = api.create_project_raw_response("")
    assert resp.status_code in [400, 422]
    print("Ошибка получена")

# ========== ТЕСТЫ ДЛЯ GET /projects/{id} ==========


def test_get_project_positive():
    """Позитивный тест получения проекта"""
    print("\n Тест: получение проекта")

    # Создаем
    create_result = api.create_project("Проект для GET")
    project_id = create_result["id"]

    # Получаем
    project = api.get_project(project_id)

    # Проверяем
    assert project["id"] == project_id
    assert project["title"] == "Проект для GET"

    # Очистка
    api.delete_project(project_id)
    print("Тест пройден")


def test_get_project_negative_not_found():
    """Негативный тест: несуществующий ID"""
    print("\n Тест: получение несуществующего проекта")

    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = api.get_project_raw_response(fake_id)
    assert resp.status_code == 404
    print("Ошибка 404 получена")

# ========== ТЕСТЫ ДЛЯ PUT /projects/{id} ==========


def test_update_project_positive():
    """Позитивный тест обновления проекта"""
    print("\n Тест: обновление проекта")

    # Создаем
    create_result = api.create_project("Старое")
    project_id = create_result["id"]

    # Обновляем
    result = api.update_project(project_id, "Новое")

    if "title" in result:
        # Если API вернул title - проверяем его
        assert result["title"] == "Новое"
    else:
        # Если API не вернул title - проверяем через GET запрос
        project = api.get_project(project_id)
        assert project["title"] == "Новое", "Название не обновилось"

    # Очистка
    api.delete_project(project_id)
    print("Тест пройден")


def test_update_project_negative_empty_title():
    """Негативный тест: обновление с пустым названием"""
    print("\n Тест: обновление с пустым названием")

    # Создаем
    create_result = api.create_project("Проект")
    project_id = create_result["id"]

    # Пытаемся обновить
    resp = api.update_project_raw_response(project_id, "")

    # Проверяем ошибку
    assert resp.status_code in [400, 422]

    # Очистка
    api.delete_project(project_id)
    print("Ошибка получена")


def test_update_project_negative_not_found():
    """Негативный тест: обновление несуществующего"""
    print("\n Тест: обновление несуществующего проекта")

    fake_id = "99999999-9999-9999-9999-999999999999"
    resp = api.update_project_raw_response(fake_id, "Название")
    assert resp.status_code == 404
    print("Ошибка 404 получена")
