# Проект тестирования UI

## Описание проекта

Тестирование веб-приложений с использованием Selenium (GRID)

## Запуск тестов

Создать виртуальное окружение `python -m venv .venv` \
Активировать виртуальное окружение `source .venv/bin/activate` \
Установить зависимости `pip install -r requirements.txt` \
Запустить тесты без GRID `sh run_tests.sh BROWSERS N`
или с GRID `sh run_tests_with_grid.sh BROWSERS N` \
где BROWSERS - названия браузеров (chrome,firefox,edge,ie) \
N - количество параллельных потоков (если не указывать, то будет "auto") \
Пример запуска тестов без GRID, браузер Chrome, в 2 потока `sh run_tests.sh chrome 2` \
Пример запуска тестов с GRID, браузеры Chrome и Firefox, в 4 потока `sh run_tests_with_grid.sh chrome,firefox 4` \
Открыть отчет `allure serve allure-results`