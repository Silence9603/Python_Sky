import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_calculator_slow():
    # Автоматическое управление ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        # Вводим задержку 45 секунд
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")
        
        # Нажимаем кнопки
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()
        
        # Ожидаем результат с таймаутом 50 секунд (больше задержки в 45 секунд)
        wait = WebDriverWait(driver, 50)
        
        # Проверяем, что в элементе .screen появилось значение "15"
        result_element = wait.until(
            EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, ".screen"), "15")
        )
        
        # Дополнительная проверка
        result_value = driver.find_element(By.CSS_SELECTOR, ".screen").get_attribute("value")
        assert result_value == "15", f"Получен результат: {result_value}"
        
    finally:
        driver.quit()