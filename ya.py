from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://vk.com/")
driver.get("https://ya.ru/")
driver.get('https://playwright.dev/')
driver.back()
driver.forward()

sleep(10)

