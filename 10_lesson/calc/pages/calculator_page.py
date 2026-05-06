from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """Класс Page Object для страницы калькулятора с задержкой"""

    # Локаторы элементов страницы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    SCREEN_RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: webdriver.Chrome, default_timeout: int = 50):
        """
        Инициализация страницы калькулятора

        Args:
            driver: Экземпляр WebDriver
            default_timeout: Таймаут ожидания по умолчанию в секундах
        """
        self.driver = driver
        self.default_timeout = default_timeout
        self.wait = WebDriverWait(driver, default_timeout)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открыть страницу калькулятора"""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
            )

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """
        Установить задержку в секундах

        Args:
            seconds: Количество секунд задержки
        """
        delay_element = self.driver.find_element(*self.DELAY_INPUT)
        delay_element.clear()
        delay_element.send_keys(str(seconds))

    @allure.step("Нажать кнопку 7")
    def click_button_7(self) -> None:
        """Нажать кнопку 7"""
        self.driver.find_element(*self.BUTTON_7).click()

    @allure.step("Нажать кнопку 8")
    def click_button_8(self) -> None:
        """Нажать кнопку 8"""
        self.driver.find_element(*self.BUTTON_8).click()

    @allure.step("Нажать кнопку +")
    def click_button_plus(self) -> None:
        """Нажать кнопку +"""
        self.driver.find_element(*self.BUTTON_PLUS).click()

    @allure.step("Нажать кнопку =")
    def click_button_equals(self) -> None:
        """Нажать кнопку ="""
        self.driver.find_element(*self.BUTTON_EQUALS).click()

    @allure.step("Ожидать результат {expected_result}")
    def wait_for_result(
            self, expected_result: str, timeout: int = None) -> None:
        """
        Ожидать появления ожидаемого результата на экране

        Args:
            expected_result: Ожидаемый результат (строка)
            timeout: Таймаут ожидания в секундах (опционально)
        """
        wait = WebDriverWait(self.driver, timeout or self.default_timeout)
        wait.until(
            EC.text_to_be_present_in_element(
                self.SCREEN_RESULT, expected_result))

    @allure.step("Получить текст результата с экрана")
    def get_result_text(self) -> str:
        """
        Получить текст результата с экрана

        Returns:
            str: Текст результата
        """
        return self.driver.find_element(*self.SCREEN_RESULT).text
