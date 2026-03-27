# Открыть браузер FireFox.
# Перейти на страницу http://the-internet.herokuapp.com/login.
# В поле username ввести значение tomsmith.
# В поле password ввести значение SuperSecretPassword!.
# Нажать кнопку Login.
# Вывести текст с зеленой плашки в консоль.
# Закрыть браузер (метод quit())

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

driver.maximize_window()

wait = WebDriverWait(driver, 10)

username_field = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#username")))
username_field.click()
username_field.send_keys("tomsmith")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

flash_message = wait.until(EC.presence_of_element_located((By.ID, "flash")))

print("Текст зеленой плашки:", flash_message.text)

sleep(3)

driver.quit()
