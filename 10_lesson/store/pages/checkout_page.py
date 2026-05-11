"""
Модуль CheckoutPage содержит класс для работы со страницей оформления заказа.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Класс для взаимодействия со страницей оформления заказа.

    Attributes:
        driver: WebDriver экземпляр для управления браузером
        wait: WebDriverWait экземпляр для ожидания элементов
    """

    # Локаторы формы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Локатор итоговой суммы
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_customer_info(
            self, first_name: str, last_name: str, postal_code: str
            ) -> None:
        """
        Заполнить форму данными покупателя.

        Args:
            first_name: Имя покупателя (str)
            last_name: Фамилия покупателя (str)
            postal_code: Почтовый индекс (str)

        Returns:
            None
        """
        # Вводим имя
        first_name_field = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_name_field.send_keys(first_name)

        # Вводим фамилию
        last_name_field = self.driver.find_element(*self.LAST_NAME_INPUT)
        last_name_field.send_keys(last_name)

        # Вводим почтовый индекс
        postal_code_field = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        postal_code_field.send_keys(postal_code)

    def click_continue(self) -> None:
        """
        Нажать кнопку Continue для продолжения оформления.

        Returns:
            None
        """
        continue_button = self.driver.find_element(*self.CONTINUE_BUTTON)
        continue_button.click()

    def get_total_amount(self) -> float:
        """
        Получить итоговую сумму из текста Total.

        Returns:
            float: Итоговая сумма заказа
        """
        # Ожидаем появления итоговой суммы
        total_element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        total_text = total_element.text
        # Извлекаем число из текста (формат: "Total: $58.29")
        total_amount = float(total_text.split("$")[1])
        return total_amount
