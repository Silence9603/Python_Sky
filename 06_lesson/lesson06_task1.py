# Перейдите на страницу http://uitestingplayground.com/ajax.
# Нажмите на синюю кнопку.
# Получите текст из зеленой плашки.
# Выведите его в консоль ("Data loaded with AJAX get request.").


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

driver.maximize_window()

wait = WebDriverWait(driver, 10)

button = driver.find_element(By.ID, "ajaxButton")
button.click()

green_label = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success")))
text = green_label.text

print(text)

driver.quit()
