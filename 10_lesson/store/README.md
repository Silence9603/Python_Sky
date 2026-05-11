# Проект автотестирования интернет-магазина SauceDemo

Этот проект содержит автоматический тест для проверки функциональности интернет-магазина [SauceDemo](https://www.saucedemo.com/). Тест написан на Python с использованием паттерна Page Object, библиотеки Selenium и Allure для формирования подробных отчётов.

## 📋 Описание теста

Тест проверяет полный сценарий оформления заказа:

1. **Авторизация** как пользователь `standard_user`.
2. **Добавление в корзину** трёх товаров:
   - Sauce Labs Backpack
   - Sauce Labs Bolt T-Shirt
   - Sauce Labs Onesie
3. **Переход в корзину** и нажатие `Checkout`.
4. **Заполнение формы** (имя, фамилия, почтовый индекс).
5. **Проверка итоговой суммы** — она должна равняться `$58.29`.

> [!IMPORTANT]
> Тест использует браузер Firefox. Убедитесь, что Firefox установлен на вашем компьютере.

## 🛠️ Используемые технологии

| Технология | Назначение |
|------------|------------|
| Python 3.14+ | Язык программирования |
| Selenium | Автоматизация браузера |
| pytest | Запуск тестов |
| Allure | Формирование отчётов |
| Page Object Pattern | Организация кода |

## 📁 Структура проекта
saucedemo_project/
├── page_objects/
│ ├── login_page.py # Страница авторизации
│ ├── inventory_page.py # Главная страница (список товаров)
│ ├── cart_page.py # Страница корзины
│ └── checkout_page.py # Страница оформления заказа
├── tests/
│ └── test_shop.py # Тест для проверки итоговой суммы
├── requirements.txt # Зависимости проекта
├── README.md # Этот файл
└── .gitignore # Исключаемые из Git файлы

## 🚀 Установка и запуск

1. Клонируйте репозиторий (или создайте проект локально)

```bash
git clone <url-репозитория>
cd saucedemo_project

2. Создайте виртуальное окружение

bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Установите зависимости

bash
pip install -r requirements.txt
Содержимое файла requirements.txt:

text
selenium==4.15.0
pytest==7.4.3
allure-pytest==2.13.2

4. Запустите тест

Обычный запуск:
bash
pytest tests/test_shop.py -v
Запуск с сохранением результатов для Allure:
bash
pytest tests/test_shop.py --alluredir=allure-results -v
