class Urls:
    base_url = 'https://stellarburgers.nomoreparties.site/api'
    register_url = f'{base_url}/auth/register'
    login_url = f'{base_url}/auth/login'
    delete_user_url = f'{base_url}/auth/user'
    change_user_data_url = f'{base_url}/auth/user'
    create_order_url = f'{base_url}/orders'
    get_user_orders = f'{base_url}/orders'


class TestData:
    test_user_password = 'Test1234'
    test_user_name = 'Max'
    creation_missing_fields = [
        {'password': 'Test1234', "name": 'Max'},
        {'email': 'mliv@yandex.ru', "name": 'Max'},
        {'email': 'mlove@yandex.ru', "password": 'Test1234'}
    ]


class ErrorsMessages:
    login_user_error_401 = 'email or password are incorrect'
    create_exists_user_error_403 = 'User already exists'
    create_user_required_fields_error_403 = 'Email, password and name are required fields'
    create_order_error_400 = 'Ingredient ids must be provided'
    authorised_error_401 = 'You should be authorised'
