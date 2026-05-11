"""
Модуль InventoryPage содержит класс для работы с главной страницей магазина.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """
    Класс для взаимодействия с главной страницей магазина (список товаров).

    Attributes:
        driver: WebDriver экземпляр для управления браузером
        wait: WebDriverWait экземпляр для ожидания элементов
    """

    # Локаторы кнопок добавления товаров
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")

    # Локатор корзины
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        """
        Инициализация главной страницы магазина.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self) -> None:
        """
        Добавить рюкзак Sauce Labs Backpack в корзину.

        Returns:
            None
        """
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_ADD_BUTTON)
        )
        add_button.click()

    def add_bolt_tshirt_to_cart(self) -> None:
        """
        Добавить футболку Sauce Labs Bolt T-Shirt в корзину.

        Returns:
            None
        """
        add_button = self.driver.find_element(*self.BOLT_TSHIRT_ADD_BUTTON)
        add_button.click()

    def add_onesie_to_cart(self) -> None:
        """
        Добавить Onesie в корзину.

        Returns:
            None
        """
        add_button = self.driver.find_element(*self.ONESIE_ADD_BUTTON)
        add_button.click()

    def go_to_cart(self) -> None:
        """
        Перейти в корзину.

        Returns:
            None
        """
        cart_icon = self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        cart_icon.click()
