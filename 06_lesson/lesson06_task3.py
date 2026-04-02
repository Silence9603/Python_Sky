# Перейдите на сайт https://bonigarcia.dev/
# selenium-webdriver-java/loading-images.html.
# Дождитесь загрузки всех картинок.
# Получите значение атрибута src у 3-й картинки.
# Выведите значение в консоль.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

WebDriverWait(driver, 10).until(
    lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 4)

images = driver.find_elements(By.TAG_NAME, "img")

third_image = images[3]
WebDriverWait(driver, 10).until(
    lambda d: images[3].get_attribute("src") != "")

third_image = images[3]
src_value = third_image.get_attribute("src")

print(src_value)

driver.quit()
