import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


class TestCalculator:
    @pytest.fixture
    def driver(self):
        """Фикстура для создания и настройки драйвера"""
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_slow_calculator_addition(self, driver):
        """Тест проверки работы калькулятора с задержкой"""
        # Создаем объект страницы
        calculator_page = CalculatorPage(driver)

        # Открываем страницу калькулятора
        calculator_page.open()

        # Вводим задержку 45 секунд
        calculator_page.set_delay(45)

        # Выполняем вычисление: 7 + 8
        calculator_page.click_button_7()
        calculator_page.click_button_plus()
        calculator_page.click_button_8()
        calculator_page.click_button_equals()

        # Ожидаем результат 15 (таймаут 50 секунд достаточно)
        calculator_page.wait_for_result("15")

        # Получаем результат для дополнительной проверки
        result = calculator_page.get_result_text()

        # Проверяем, что результат соответствует ожидаемому
        assert result == "15", f"Получен результат'{result}'"
