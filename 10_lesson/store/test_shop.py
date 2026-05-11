"""
Модуль с тестами для интернет-магазина SauceDemo.
Содержит тесты проверки функциональности магазина с использованием Page Object.
"""

import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин SauceDemo")
@allure.story("Проверка оформления заказа")
@allure.severity(allure.severity_level.CRITICAL)
class TestSaucedemoShop:
    """
    Класс с тестами для интернет-магазина SauceDemo.
    """

    @allure.title("Проверка итоговой суммы в корзине")
    @allure.description("""
        Тест проверяет корректность расчета итоговой суммы в корзине.

        Шаги:
        1. Открыть сайт магазина
        2. Авторизоваться как standard_user
        3. Добавить 3 товара в корзину
        4. Перейти в корзину
        5. Нажать Checkout
        6. Заполнить форму данными
        7. Получить итоговую сумму
        8. Проверить, что сумма равна $58.29
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_total_price_check(self):
        """
        Тест проверки итоговой суммы в корзине.

        Returns:
            None
        """
        with allure.step("Настройка браузера Firefox"):
            options = Options()
            driver = webdriver.Firefox(options=options)

        try:
            with allure.step("Создание объектов Page Object"):
                login_page = LoginPage(driver)
                inventory_page = InventoryPage(driver)
                cart_page = CartPage(driver)
                checkout_page = CheckoutPage(driver)

            with allure.step("Открытие сайта магазина"):
                login_page.open()

            with allure.step("Авторизация пользователем standard_user"):
                login_page.login("standard_user", "secret_sauce")

            with allure.step("Добавление товаров в корзину"):
                with allure.step("Добавление Sauce Labs Backpack"):
                    inventory_page.add_backpack_to_cart()

                with allure.step("Добавление Sauce Labs Bolt T-Shirt"):
                    inventory_page.add_bolt_tshirt_to_cart()

                with allure.step("Добавление Sauce Labs Onesie"):
                    inventory_page.add_onesie_to_cart()

            with allure.step("Переход в корзину"):
                inventory_page.go_to_cart()

            with allure.step("Ожидание загрузки страницы корзины"):
                cart_page.wait_for_cart_load()

            with allure.step("Нажатие кнопки Checkout"):
                cart_page.proceed_to_checkout()

            with allure.step("Заполнение формы данными покупателя"):
                checkout_page.fill_customer_info("Иван", "Иванов", "123456")

            with allure.step("Нажатие кнопки Continue"):
                checkout_page.click_continue()

            with allure.step("Получение итоговой суммы"):
                total_amount = checkout_page.get_total_amount()

            with allure.step("Проверка итоговой суммы"):
                expected_total = 58.29
                assert total_amount == expected_total, \
                    f"Итоговая сумма ${total_amount}, а не ${expected_total}"

                allure.attach(
                    str(total_amount),
                    name="Итоговая сумма",
                    attachment_type=allure.attachment_type.TEXT
                )

            allure.attach(
                "Тест успешно пройден",
                name="Результат теста",
                attachment_type=allure.attachment_type.TEXT
            )

        except Exception:
            with allure.step("Сохранение скриншота при ошибке"):
                driver.save_screenshot("error_screenshot.png")
                with open("error_screenshot.png", "rb") as screenshot:
                    allure.attach(
                        screenshot.read(),
                        name="Скриншот ошибки",
                        attachment_type=allure.attachment_type.PNG
                    )
            raise

        finally:
            with allure.step("Закрытие браузера"):
                driver.quit()
