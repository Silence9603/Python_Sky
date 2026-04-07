import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# @pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_data_types_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "email": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # # Заполнение полей
    # for name, value in form_data.items():
    #     field = driver.find_element(By.NAME, name)
    #     field.clear()
    #     if value:
    #         field.send_keys(value)

    # Нажать кнопку Submit
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "is-valid"))
    )

    # Проверка подсветки поля Zip code (красный - класс is-invalid)
    zip_field = driver.find_element(By.NAME, "zip-code")
    zip_classes = zip_field.get_attribute("class")
    assert "is-invalid" in zip_classes, "Zip code field should be highlighted in red (is-invalid)"

    # Список полей, которые должны быть подсвечены зелёным
    valid_fields = ["first-name", "last-name", "address", "email", "phone", "city", "country", "job-position", "company"]

    for field_name in valid_fields:
        field = driver.find_element(By.NAME, field_name)
        field_classes = field.get_attribute("class")
        assert "is-valid" in field_classes, f"Field {field_name} should be highlighted in green (is-valid), but got {field_classes}"
