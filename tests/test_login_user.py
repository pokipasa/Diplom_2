import requests
import allure
import pytest

from data import Urls, TestData
from data import ErrorsMessages


class TestLoginUser:

    @allure.title('Проверка успешного входа пользователя в систему')
    def test_successful_login(self, create_user):
        payload = {'email': create_user[1],
                   'password': TestData.TEST_USER_PASSWORD
                   }
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.post(Urls.LOGIN_URL, data=payload, headers=headers)
        assert response.status_code == 200
        assert response.json().get('success') is True
        assert 'user' in response.json()
        assert 'accessToken' in response.json()
        user_data = response.json()['user']
        assert 'email' in user_data
        assert 'name' in user_data
        assert 'refreshToken' in response.json()

    @allure.title('Проверка неудачной авторизации пользователя, при неправильно введённых email или пароле')
    @pytest.mark.parametrize('invalid_data', ['email', 'password'])
    def test_invalid_email_or_password(self, create_user, invalid_data):
        payload = {
            'email': create_user[0],
            'password': TestData.TEST_USER_PASSWORD
        }
        payload[invalid_data] = f'{payload[invalid_data]}a'
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.post(Urls.LOGIN_URL, data=payload, headers=headers)
        assert response.status_code == 401
        assert response.json().get('success') is False
        assert response.json()['message'] == ErrorsMessages.LOGIN_USER_ERROR_401
