from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    # Локаторы
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        """Добавить рюкзак в корзину"""
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_ADD_BUTTON)
        )
        add_button.click()

    def add_bolt_tshirt_to_cart(self):
        """Добавить футболку Bolt в корзину"""
        add_button = self.driver.find_element(*self.BOLT_TSHIRT_ADD_BUTTON)
        add_button.click()

    def add_onesie_to_cart(self):
        """Добавить Onesie в корзину"""
        add_button = self.driver.find_element(*self.ONESIE_ADD_BUTTON)
        add_button.click()

    def go_to_cart(self):
        """Перейти в корзину"""
        cart_icon = self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        )
        cart_icon.click()
