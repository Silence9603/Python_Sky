import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestSaucedemoShop:

    @pytest.fixture
    def driver(self):
        # Фикстура для создания и настройки драйвера Firefox
        options = Options()
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

        yield driver
        driver.quit()

    def test_total_price_check(self, driver):
        # Тест проверки итоговой суммы в корзине
        # Создаем объекты страниц
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Открыть сайт магазина
        login_page.open()

        # Авторизоваться как пользователь standard_user
        login_page.login("standard_user", "secret_sauce")

        # Добавить в корзину товары
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bolt_tshirt_to_cart()
        inventory_page.add_onesie_to_cart()

        # Перейти в корзину
        inventory_page.go_to_cart()

        # Ожидаем загрузки страницы корзины
        cart_page.wait_for_cart_load()

        # Нажать кнопку Checkout
        cart_page.proceed_to_checkout()

        # Заполнить форму данными
        checkout_page.fill_customer_info("Иван", "Иванов", "123456")

        # Нажать кнопку Continue
        checkout_page.click_continue()

        # Прочитать итоговую стоимость
        total_amount = checkout_page.get_total_amount()

        # Проверить, что итоговая сумма равна $58.29
        expected_total = 58.29
        assert total_amount == expected_total, \
            f"Итоговая сумма ${total_amount} не равна ${expected_total}"

        print(f"\n✅ Тест пройден! Итоговая сумма: ${total_amount}")
