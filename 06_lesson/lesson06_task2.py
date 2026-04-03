from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Настройка драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.ID, "newButtonName")
input_field.clear()
input_field.send_keys("SkyPro")


button = driver.find_element(By.ID, "updatingButton")
button.click()


updated_button = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro"))
button_text = driver.find_element(By.ID, "updatingButton").text

print(button_text)

driver.quit()
