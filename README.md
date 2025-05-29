# Блок U. UI autotests

## Инструкция по запуску тестов

1. Клонировать репозиторий `git clone https://github.com/sdet0mis/ss-ui.git`
2. Перейти в директорию репозитория `cd ss-ui`
3. Создать виртуальное окружение `python -m venv .venv`
4. Активировать виртуальное окружение `source .venv/bin/activate`
5. Установить зависимости `pip install -r requirements.txt`
6. Запустить тесты `pytest --alluredir=allure-results`
7. Открыть отчет `allure serve allure-results`