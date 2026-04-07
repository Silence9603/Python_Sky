import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFormValidation:
    def test_form_validation(self):
        driver = webdriver.Edge()
        
        try:
            # Открытие страницы
            driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
            driver.maximize_window()
            
            # Заполнение формы
            # First name
            first_name = driver.find_element(By.NAME, "first-name")
            first_name.send_keys("Иван")
            
            # Last name
            last_name = driver.find_element(By.NAME, "last-name")
            last_name.send_keys("Петров")
            
            # Address
            address = driver.find_element(By.NAME, "address")
            address.send_keys("Ленина, 55-3")
            
            # Email
            email = driver.find_element(By.NAME, "e-mail")
            email.send_keys("test@skypro.com")
            
            # Phone number
            phone = driver.find_element(By.NAME, "phone")
            phone.send_keys("+7985899998787")
            
            # Zip code (оставляем пустым)
            zip_code = driver.find_element(By.NAME, "zip-code")
            zip_code.send_keys("")
            
            # City
            city = driver.find_element(By.NAME, "city")
            city.send_keys("Москва")
            
            # Country
            country = driver.find_element(By.NAME, "country")
            country.send_keys("Россия")
            
            # Job position
            job_position = driver.find_element(By.NAME, "job-position")
            job_position.send_keys("QA")
            
            # Company
            company = driver.find_element(By.NAME, "company")
            company.send_keys("SkyPro")
            
            # Нажатие кнопки Submit
            submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()

            # Ожидание применения стилей после отправки
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "alert"))
            )
            
            # Проверка, что поле Zip code подсвечено красным
            zip_code_field = driver.find_element(By.NAME, "zip-code")
            zip_code_class = zip_code_field.get_attribute("class")
            assert "error" in zip_code_class or "is-invalid" in zip_code_class.lower(), \
                f"Zip code field should be highlighted red, but got class: {zip_code_class}"
            
            # Список полей, которые должны быть подсвечены зеленым
            green_fields = [
                ("first-name", "First name"),
                ("last-name", "Last name"),
                ("address", "Address"),
                ("e-mail", "Email"),
                ("phone", "Phone number"),
                ("city", "City"),
                ("country", "Country"),
                ("job-position", "Job position"),
                ("company", "Company")
            ]
            
            # Проверка каждого поля на зеленую подсветку
            for field_name, field_label in green_fields:
                field = driver.find_element(By.NAME, field_name)
                field_class = field.get_attribute("class")
                assert "success" in field_class or "is-valid" in field_class.lower(), \
                    f"Field '{field_label}' should be highlighted green, but got class: {field_class}"
            
            print("Все проверки успешно пройдены!")
            
        finally:
            # Закрытие браузера
            driver.quit()
