# Импортируем класс из файла MainPage, который лежит в папке pages:
from les7_train.labirint.pages.MainPage import MainPage
from selenium import webdriver
from les7_train.labirint.pages.ResultPage import ResultPage
from les7_train.labirint.pages.CartPage import CartPage

def test_cart_counter(): 
    browser = webdriver.Chrome()  # Открываем браузер
    main_page = MainPage(browser)  # Переменная хранит экземпляр класса MainPage
    main_page.set_cookie_policy()  # Вызываем метод set_cookie_policy из MainPage

def __init__(self, driver):
    self._driver = driver

def test_cart_counter():
    browser = webdriver.Chrome()
    main_page = MainPage(browser) 
    main_page.set_cookie_policy()
    main_page.search("Python")

    result_page = ResultPage(browser)
    # result_page.switch_to_table()  # Используем только в видео, больше не актуально
    result_page.add_books()

def test_cart_counter():
    browser = webdriver.Chrome()
    main_page = MainPage(browser) 
    main_page.set_cookie_policy()
    main_page.search("Python")

    result_page = ResultPage(browser)
    # result_page.switch_to_table()  # Используем только в видео
    to_be = result_page.add_books()  # Результат вызова add_books

    cart_page = CartPage(browser)
    cart_page.get()  # Переход на страницу с корзиной
    as_is = cart_page.get_counter()  # Текущее значение счетчика на странице 

    assert as_is == to_be
    browser.quit()
