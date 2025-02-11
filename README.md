Выпускной проект. Задание 2: API
Автоматические тесты для проверки API эндпоинтов Stellar Burgers.
Организация проекта:
папка tests - включает тесты, разделенные на несколько модулей:

test_create_user.py
Проверяет эндпоинт "Регистрация пользователя" POST /api/auth/register.

Класс TestCreateUser включает следующие тесты:

test_successful_user_creation

test_create_exists_user

test_create_user_with_missing_field

test_login_user.py
Проверяет эндпоинт "Вход пользователя" POST /api/auth/login.

Класс TestLoginUser включает следующие тесты:

test_successful_login

test_invalid_email_or_password

test_change_user_data.py
Проверяет эндпоинт "Изменение данных пользователя" PATCH /api/auth/user.

Класс TestChangeUserData включает следующие тесты:

test_successful_user_data_change_with_auth

test_failed_user_data_change_without_auth

test_create_order.py
Проверяет эндпоинт "Создание нового заказа" POST /api/v1/orders.

Класс TestCreateOrder включает следующие тесты:

test_create_order_with_authorization_and_ingredients

test_create_order_without_authorization

test_create_order_without_ingredients

test_order_creation_with_wrong_ingredients_hash_failed

test_get_user_orders.py
Проверяет эндпоинт "Получение заказов пользователя" GET /api/orders.

Класс TestGetUserOrders включает следующие тесты:

test_get_user_orders_with_authorization

test_get_user_orders_without_authorization

conftest.py
Содержит фикстуру create_user.

В корне проекта находятся:
файл data.py с данными для тестирования,
файл requirements.txt со списком зависимостей
и файл .gitignore.

Как запустить автотесты:

Установка необходимых пакетов
$ pip install -r requirements.txt
Создание Allure-отчёта

$ pytest tests --alluredir=allure_results
$ allure serve allure_results