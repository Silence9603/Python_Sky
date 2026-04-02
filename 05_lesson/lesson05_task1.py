# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/classattr.
# Кликнуть на синюю кнопку.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr/")
btn_primary = '.btn-primary'
search_input = driver.find_element(By.CSS_SELECTOR, btn_primary)
search_input.send_keys(Keys.RETURN)

sleep(10)
