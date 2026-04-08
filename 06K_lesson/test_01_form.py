from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService


class TestFormValidation:
    def test_form_validation(self):
        driver_path = r"Edge\edgedriver.exe"
        service = EdgeService(executable_path=driver_path)
        driver = webdriver.Edge(service=service)

        try:
            driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/"
                + "data-types.html"
            )
            driver.maximize_window()

            # Заполнение формы
            first_name = driver.find_element(By.NAME, "first-name")
            first_name.send_keys("Иван")

            last_name = driver.find_element(By.NAME, "last-name")
            last_name.send_keys("Петров")

            address = driver.find_element(By.NAME, "address")
            address.send_keys("Ленина, 55-3")

            email = driver.find_element(By.NAME, "e-mail")
            email.send_keys("test@skypro.com")

            phone = driver.find_element(By.NAME, "phone")
            phone.send_keys("+7985899998787")

            zip_code = driver.find_element(By.NAME, "zip-code")
            zip_code.send_keys("")

            city = driver.find_element(By.NAME, "city")
            city.send_keys("Москва")

            country = driver.find_element(By.NAME, "country")
            country.send_keys("Россия")

            job_position = driver.find_element(By.NAME, "job-position")
            job_position.send_keys("QA")

            company = driver.find_element(By.NAME, "company")
            company.send_keys("SkyPro")

            # Нажатие кнопки Submit
            submit_button = driver.find_element(
                By.CSS_SELECTOR, "button[type='submit']"
            )
            submit_button.click()

            # Ожидание применения стилей после отправки
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "alert"))
            )

            # Проверка, что поле Zip code подсвечено красным
            zip_code_field = driver.find_element(By.ID, "zip-code")  # Найти ID
            zip_code_class = zip_code_field.get_attribute("class")
            assert (
                "danger" in zip_code_class.lower()
            ), f"Поле должно быть красным, но оно {zip_code_class}"

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
                ("company", "Company"),
            ]

            # Проверка каждого поля на зеленую подсветку
            for field_name, field_label in green_fields:
                field = driver.find_element(By.ID, field_name)
                field_class = field.get_attribute("class")
                assert (
                    "success" in field_class.lower()
                ), f"Поле '{field_label}' должно быть зелёным, но оно {field_class}"

        finally:
            # Закрытие браузера
            driver.quit()
