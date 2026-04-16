from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    # Локаторы
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def wait_for_cart_load(self):
        """Ожидать загрузки страницы корзины"""
        self.wait.until(
            EC.presence_of_element_located(self.CART_LIST)
        )
    
    def proceed_to_checkout(self):
        """Нажать кнопку Checkout"""
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()
