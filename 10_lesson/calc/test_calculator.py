import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@allure.epic("Калькулятор")
@allure.feature("Арифметические операции")
@allure.severity(allure.severity_level.NORMAL)
class TestCalculator:
    """Тестовый класс для проверки функциональности калькулятора"""

    @pytest.fixture
    def driver(self) -> webdriver.Chrome:
        """
        Фикстура для создания и настройки драйвера

        Returns:
            webdriver.Chrome: Настроенный экземпляр WebDriver
        """
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.id("CALC-1")
    @allure.title("Проверка сложения с задержкой")
    @allure.description(
        "Тест проверяет работу калькулятора с задержкой 45 секунд")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_slow_calculator_addition(self, driver: webdriver.Chrome) -> None:
        """
        Тест проверки работы калькулятора с задержкой

        Args:
            driver: Экземпляр WebDriver
        """
        with allure.step("Создать объект страницы калькулятора"):
            calculator_page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            calculator_page.open()

        with allure.step("Установить задержку 45 секунд"):
            calculator_page.set_delay(45)

        with allure.step("Ввести выражение 7 + 8"):
            calculator_page.click_button_7()
            calculator_page.click_button_plus()
            calculator_page.click_button_8()
            calculator_page.click_button_equals()

        with allure.step("Проверить, что результат равен 15"):
            calculator_page.wait_for_result("15")

        with allure.step("Получить итоговый результат для доп проверки"):
            result = calculator_page.get_result_text()

        with allure.step("Выполнить финальную проверку результата"):
            assert result == "15", f"Получен результат '{result}', а не '15'"
