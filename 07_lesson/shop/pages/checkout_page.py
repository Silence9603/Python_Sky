from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # Локаторы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_customer_info(self, first_name, last_name, postal_code):
        """Заполнить форму данными покупателя"""
        first_name_field = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(*self.LAST_NAME_INPUT)
        last_name_field.send_keys(last_name)

        postal_code_field = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        postal_code_field.send_keys(postal_code)

    def click_continue(self):
        """Нажать кнопку Continue"""
        continue_button = self.driver.find_element(*self.CONTINUE_BUTTON)
        continue_button.click()

    def get_total_amount(self):
        """Получить итоговую сумму из текста Total"""
        total_element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        total_text = total_element.text
        # Извлечение числа из текста (формат: "Total: $58.29")
        total_amount = float(total_text.split("$")[1])
        return total_amount
