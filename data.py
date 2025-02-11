class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'
    REGISTER_URL = f'{BASE_URL}/auth/register'
    LOGIN_URL = f'{BASE_URL}/auth/login'
    DELETE_USER_URL = f'{BASE_URL}/auth/user'
    CHANGE_USER_DATA_URL = f'{BASE_URL}/auth/user'
    CREATE_ORDER_URL = f'{BASE_URL}/orders'
    GET_USER_ORDERS = f'{BASE_URL}/orders'


class TestData:
    TEST_USER_PASSWORD = 'Test1234'
    TEST_USER_NAME = 'Max'
    CREATION_MISSING_FIELDS = [
        {'password': 'Test1234', "name": 'Max'},
        {'email': 'mliv@yandex.ru', "name": 'Max'},
        {'email': 'mlove@yandex.ru', "password": 'Test1234'}
    ]


class ErrorsMessages:
    LOGIN_USER_ERROR_401 = 'email or password are incorrect'
    CREATE_EXISTS_USER_ERROR_403 = 'User already exists'
    CREATE_USER_REQUIRED_FIELDS_ERROR_403 = 'Email, password and name are required fields'
    CREATE_ORDER_ERROR_400 = 'Ingredient ids must be provided'
    AUTHORISED_ERROR_401 = 'You should be authorised'
