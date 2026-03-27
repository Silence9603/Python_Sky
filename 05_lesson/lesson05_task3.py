# Открыть браузер FireFox
# Перейти на страницу: http://the-internet.herokuapp.com/inputs.
# Ввести в поле текст 12345
# Очистить это поле (метод clear()).
# Ввести в поле текст 54321
# Закрыть браузер (метод quit())

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    driver.maximize_window()

    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, "input[type='number']")))

    input_field.send_keys("12345")
    print("Введено: 12345")

    sleep(2)

    input_field.clear()
    print("Поле очищено")

    sleep(2)

    input_field.send_keys("54321")
    print("Введено: 54321")

    sleep(2)  # чтобы увидеть результат

finally:
    driver.quit()
