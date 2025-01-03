# Проект Diplom_2: Тестирование API

## Описание проекта
Этот проект создан для автоматизации тестирования API сервиса **Stellar Burgers**.
Проект реализует тесты для проверки ключевых функций API, таких как регистрация пользователей, авторизация, создание заказов и получение истории заказов.
Все тесты написаны с использованием **pytest** и **requests**, а для генерации отчетов используется **Allure**.

## Установка

Для установки необходимых зависимостей выполните следующие шаги:

1. Клонируйте репозиторий на локальную машину:
   ```bash
   git clone https://github.com/CRASH3000/Diplom_2.git
   ```
   ```bash
   cd Diplom_2
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Запуск тестов и генерация Allure отчета

Для запуска тестов и генерации отчета Allure выполните следующие команды:

1. Запуск тестов:
   ```bash
   pytest --alluredir=allure-results
   ```

   Альтернативная команда для запуска тестов:
   ```bash
   PYTHONPATH=$(pwd) pytest --alluredir=allure-results
   ```

   Так же тесты можно запустить без отчета использовав команду:
    ```bash
    pytest tests
    ```

    Для запуска конкретного теста:
     ```bash
     pytest tests/test_01_create_user.py::test_create_unique_user
     ```

2. Генерация и просмотр отчета Allure:
   ```bash
   allure serve allure-results
   ```
## Структура проекта

- **tests/**: Содержит файлы с тестовыми сценариями.
- **data/**: Хранит URL и сообщения со статусами.
- **conftest.py**: Фикстуры для тестов, такие как базовый URL, авторизация, данные ингредиентов и данные пользователей.
- **requirements.txt**: Список зависимостей для проекта.
- **allure-results/**: Директория для хранения результатов тестирования Allure.

## Список тестов (Проверки)

### Создание пользователя:
- Создание уникального пользователя.
- Создание уже зарегистрированного пользователя.
- Создание пользователя без обязательного поля (например, без имени).

### Логин пользователя:
- Логин под существующим пользователем.
- Логин с неверными данными (неверный логин или пароль).

### Изменение данных пользователя:
- Изменение данных с авторизацией (проверка возможности изменить любое поле).
- Изменение данных без авторизации (проверка, что система вернет ошибку).

### Создание заказа:
- Создание заказа с авторизацией.
- Создание заказа без авторизации.
- Создание заказа с корректными ингредиентами.
- Создание заказа без указания ингредиентов.
- Создание заказа с неверным хешем ингредиентов.

### Получение заказов конкретного пользователя:
- Получение истории заказов авторизованного пользователя.
- Попытка получения истории заказов без авторизации (ожидание ошибки).

## Важные моменты:
- Тестовые данные для пользователей и заказов создаются перед каждым тестом и удаляются после выполнения.
