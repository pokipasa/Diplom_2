import requests
import allure
import pytest

from data import Urls, TestData
from data import ErrorsMessages


class TestCreateUser:

    @allure.title('Проверка успешного создания пользователя')
    def test_successful_user_creation(self, create_user):
        response = create_user[0]
        assert response.status_code == 200
        assert response.json().get('success') is True
        assert 'user' in response.json()
        assert 'accessToken' in response.json()
        user_data = response.json()['user']
        assert 'email' in user_data
        assert 'name' in user_data
        assert 'refreshToken' in response.json()

    @allure.title('Проверка повторного создания существующего пользователя')
    def test_create_exists_user(self, create_user):
        repeating_user_payload = {
            "email": f'{create_user[1]}',
            "password": TestData.test_user_password,
            "name": TestData.test_user_name
        }
        response = requests.post(Urls.register_url, data=repeating_user_payload)
        assert response.status_code == 403
        assert response.json().get('success') is False
        assert response.json()['message'] == ErrorsMessages.create_exists_user_error_403

    @allure.title('Проверка создания пользователя с отсутствующими полями')
    @pytest.mark.parametrize('payload', TestData.creation_missing_fields)
    def test_create_user_with_missing_field(self, payload):
        response = requests.post(Urls.register_url, data=payload)
        assert response.status_code == 403
        assert response.json().get('success') is False
        assert response.json()['message'] == ErrorsMessages.create_user_required_fields_error_403
