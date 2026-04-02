# from time import sleep
# from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service as ChromeService
# # from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

# browser = webdriver.Firefox()

# #три строки ниже - новые, импорт драйвера для Firefox
# # from selenium.webdriver.firefox.service import Service as FirefoxService
# # from webdriver_manager.firefox import GeckoDriverManager
# # browser = webdriver.Firefox(  #поменяли название переменной driver на browser
# # service=FirefoxService(GeckoDriverManager().install()))

# # browser = webdriver.Chrome(service=ChromeService(
# # ChromeDriverManager().install()))

# browser.maximize_window() #для разворачивания окна
# browser.get("https://ya.ru/") #для перехода на нужную страницу
# sleep(5) #для паузы на загрузку контента страницы
# browser.save_screenshot("./ya.png") #для сохранения скриншота
# browser.quit() #для закрытия окна


from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

chrome = webdriver.Chrome()
ff = webdriver.Firefox()
edge = webdriver.Edge()

def make_screenshot(browser):
	browser.maximize_window()
	browser.get("https://ya.ru/")
	sleep(5)
	browser.save_screenshot("./ya_"+browser.name+".png")
	browser.quit()

make_screenshot(chrome)
make_screenshot(ff)
make_screenshot(edge)