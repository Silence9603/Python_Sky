# Проект автотестирования калькулятора с задержкой

Этот проект содержит автоматический тест для проверки функциональности калькулятора на сайте [Slow Calculator](https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html). Тест написан на Python с использованием паттерна Page Object и библиотеки Selenium.

## 📋 Описание теста

Тест выполняет следующие шаги:
1. Открывает страницу калькулятора.
2. Устанавливает задержку в `45` секунд.
3. Нажимает кнопки: `7`, `+`, `8`, `=`.
4. Ожидает результат `15`.
5. Проверяет, что результат действительно равен `15`.

> [!NOTE]
> Калькулятор имеет искусственную задержку перед отображением результата. Тест учитывает это с помощью явного ожидания.

## 🛠️ Используемые технологии

| Технология | Назначение |
|------------|------------|
| Python 3.14+ | Язык программирования |
| Selenium | Автоматизация браузера |
| pytest | Запуск тестов |
| WebDriver Manager | Автоматическое управление драйверами |
| Page Object Pattern | Организация кода |

## 📁 Структура проекта
calculator_project/
├── page_objects/
│ └── calculator_page.py # Класс с методами для работы с калькулятором
├── tests/
│ └── test_calculator.py # Тест для проверки сложения
├── requirements.txt # Зависимости проекта
└── README.md # Этот файл

## 🚀 Установка и запуск

1. Клонируйте репозиторий (или создайте проект локально)

```bash
git clone <url-репозитория>
cd calculator_project

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
webdriver-manager==4.0.1

4. Запустите тест

bash
pytest tests/test_calculator.py -v
Для запуска с выводом print:

bash
pytest tests/test_calculator.py -v -s
