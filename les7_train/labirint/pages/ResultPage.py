from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, browser):
        self.driver = browser

    def add_books(self):
        buy_buttons = self.driver.find_elements(
            By.CSS_SELECTOR, "[data-carttext]"
        )

        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1

        return counter