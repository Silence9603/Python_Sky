from selenium import webdriver
from selenium.webdriver.common.by import By

cookie = {"name": "cookie_policy", "value": "1"}

def test_card_counter():
  browser = webdriver.Chrome()

  # Перейти на сайт «Лабиринта»
  def open_labirint():
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

  # Найти все книги по слову python
  def search(term):
    browser.find_element(
      By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

  # Добавить все книги на первой странице в корзину и посчитать
  def add_books():
    buy_buttons = browser.find_elements(
      By.CSS_SELECTOR, "[data-carttext]")

    counter = 0
    for btn in buy_buttons:
      btn.click()
      counter += 1

    return counter

  # Перейти в корзину
  def go_to_cart():
  # Переходим в корзину
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
  # Проверяем счетчик книг. Должен быть равен числу нажатий
  txt = browser.find_element(By.ID, 'basket-default-prod-count2').text
  # Возвращаем число
  return int(txt.split()[0])

def close_driver():
  # Закрываем браузер
  browser.quit()
