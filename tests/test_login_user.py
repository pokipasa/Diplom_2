import requests
import allure
import pytest

from data import Urls, TestData
from data import ErrorsMessages


class TestLoginUser:

    @allure.title('Проверка успешной авторизации пользователя')
    def test_successful_login(self, create_user):
        payload = {'email': create_user[1],
                   'password': TestData.test_user_password
                   }
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.post(Urls.login_url, data=payload, headers=headers)
        assert response.status_code == 200
        assert response.json().get('success') is True
        assert 'user' in response.json()
        assert 'accessToken' in response.json()
        user_data = response.json()['user']
        assert 'email' in user_data
        assert 'name' in user_data
        assert 'refreshToken' in response.json()

    @allure.title('Проверка неуспешной авторизации пользователя, если неправильно указать email или пароль')
    @pytest.mark.parametrize('invalid_data', ['email', 'password'])
    def test_invalid_email_or_password(self, create_user, invalid_data):
        payload = {
            'email': create_user[0],
            'password': TestData.test_user_password
        }
        payload[invalid_data] = f'{payload[invalid_data]}a'
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.post(Urls.login_url, data=payload, headers=headers)
        assert response.status_code == 401
        assert response.json().get('success') is False
        assert response.json()['message'] == ErrorsMessages.login_user_error_401
