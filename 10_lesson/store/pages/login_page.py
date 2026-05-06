"""
Модуль LoginPage содержит класс для работы со страницей авторизации.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Класс для взаимодействия со страницей авторизации SauceDemo.

    Attributes:
        driver: WebDriver экземпляр для управления браузером
        wait: WebDriverWait экземпляр для ожидания элементов
    """

    # Локаторы элементов на странице авторизации
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """
        Открыть страницу авторизации.

        Returns:
            None
        """
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def login(self, username: str, password: str) -> None:
        """
        Выполнить авторизацию с указанными учетными данными.

        Args:
            username: Имя пользователя (str)
            password: Пароль пользователя (str)

        Returns:
            None
        """
        # Вводим логин
        username_field = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        )
        username_field.send_keys(username)

        # Вводим пароль
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.send_keys(password)

        # Нажимаем кнопку входа
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

        # Ожидаем загрузки главной страницы (появление списка товаров)
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
