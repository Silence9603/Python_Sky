from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


class TestSaucedemoShop:

    def test_total_price_check(self):
        options = Options()
        driver = webdriver.Firefox(options=options)

        try:
            # Открыть сайт
            driver.get("https://www.saucedemo.com/")
            driver.maximize_window()

            wait = WebDriverWait(driver, 10)

            # Авторизоваться как standard_user
            username_field = wait.until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )
            username_field.send_keys("standard_user")

            password_field = driver.find_element(By.ID, "password")
            password_field.send_keys("secret_sauce")

            login_button = driver.find_element(By.ID, "login-button")
            login_button.click()

            wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "inventory_list")
                )
            )

            # Добавить в корзину товары
            backpack_add_button = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "add-to-cart-sauce-labs-backpack")
                )
            )
            backpack_add_button.click()

            bolt_tshirt_add_button = driver.find_element(
                By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
            )
            bolt_tshirt_add_button.click()

            onesie_add_button = driver.find_element(
                By.ID, "add-to-cart-sauce-labs-onesie"
            )
            onesie_add_button.click()

            # Перейти в корзину
            cart_icon = wait.until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "shopping_cart_link")
                )
            )
            cart_icon.click()

            # Ожидание загрузки страницы корзины
            wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
            )

            # Нажать Checkout
            checkout_button = wait.until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            checkout_button.click()

            # Заполнить форму своими данными
            first_name_field = wait.until(
                EC.presence_of_element_located((By.ID, "first-name"))
            )
            first_name_field.send_keys("Иван")

            last_name_field = driver.find_element(By.ID, "last-name")
            last_name_field.send_keys("Иванов")

            postal_code_field = driver.find_element(By.ID, "postal-code")
            postal_code_field.send_keys("123456")

            # Нажать кнопку Continue
            continue_button = driver.find_element(By.ID, "continue")
            continue_button.click()

            # Прочитать со страницы итоговую стоимость (Total)
            total_element = wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "summary_total_label")
                )
            )
            total_text = total_element.text

            # Извлечение числа из текста (формат: "Total: $58.29")
            total_amount = total_text.split("$")[1]
            total_amount_float = float(total_amount)

            # Проверить, что итоговая сумма равна $58.29
            expected_total = 58.29
            assert (
                total_amount_float == expected_total
            ), f"Итоговая сумма {total_amount_float} не равна {expected_total}"

            print(f"\n✅ Тест пройден! Итоговая сумма: ${total_amount_float}")

        except Exception as e:
            print(f"\n❌ Ошибка в тесте: {e}")
            # Делаем скриншот при ошибке
            driver.save_screenshot("error_screenshot.png")
            raise
        finally:
            # Закрытие браузера
            driver.quit()
