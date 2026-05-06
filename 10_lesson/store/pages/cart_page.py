"""
Модуль CartPage содержит класс для работы со страницей корзины.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Класс для взаимодействия со страницей корзины.

    Attributes:
        driver: WebDriver экземпляр для управления браузером
        wait: WebDriverWait экземпляр для ожидания элементов
    """

    # Локаторы
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_LIST = (By.CLASS_NAME, "cart_list")

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_cart_load(self) -> None:
        """
        Ожидать загрузки страницы корзины.

        Returns:
            None
        """
        self.wait.until(
            EC.presence_of_element_located(self.CART_LIST)
        )

    def proceed_to_checkout(self) -> None:
        """
        Нажать кнопку Checkout для перехода к оформлению заказа.

        Returns:
            None
        """
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()
