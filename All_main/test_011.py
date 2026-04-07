import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class TestFormValidation:
    def test_form_validation(self):
        # Автоматическая установка и обновление драйвера
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        
        try:
            # Открытие страницы с таймаутом
            driver.set_page_load_timeout(30)
            driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
            driver.maximize_window()
            
            # Заполнение формы
            driver.find_element(By.NAME, "first-name").send_keys("Иван")
            driver.find_element(By.NAME, "last-name").send_keys("Петров")
            driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
            driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
            driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
            driver.find_element(By.NAME, "zip-code").send_keys("")
            driver.find_element(By.NAME, "city").send_keys("Москва")
            driver.find_element(By.NAME, "country").send_keys("Россия")
            driver.find_element(By.NAME, "job-position").send_keys("QA")
            driver.find_element(By.NAME, "company").send_keys("SkyPro")
            
            # Нажатие кнопки Submit
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(1)
            
            # Проверка Zip code (должен быть красным)
            zip_code = driver.find_element(By.NAME, "zip-code")
            zip_code_class = zip_code.get_attribute("class")
            assert "error" in zip_code_class or "is-invalid" in zip_code_class.lower(), \
                f"Zip code должен быть красным. Класс: {zip_code_class}"
            
            # Проверка остальных полей (должны быть зелеными)
            fields = ["first-name", "last-name", "address", "e-mail", 
                     "phone", "city", "country", "job-position", "company"]
            
            for field_name in fields:
                field = driver.find_element(By.NAME, field_name)
                field_class = field.get_attribute("class")
                assert "success" in field_class or "is-valid" in field_class.lower(), \
                    f"Поле {field_name} должно быть зеленым. Класс: {field_class}"
            
            print("✓ Тест успешно пройден!")
            
        except Exception as e:
            print(f"Ошибка: {e}")
            raise
        finally:
            driver.quit()