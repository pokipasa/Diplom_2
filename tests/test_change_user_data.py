import requests
import allure
import pytest

from data import Urls, TestData
from data import ErrorsMessages


class TestChangeUserData:

    @allure.title('Тестирование успешного обновления профиля пользователя с авторизацией')
    @pytest.mark.parametrize('changed_field', ['email', 'password', 'name'])
    def test_user_data_update_success_with_authentication(self, create_user, changed_field):
        payload = {'email': create_user[1],
                   'password': TestData.TEST_USER_PASSWORD,
                   'name': TestData.TEST_USER_NAME
                   }
        payload[changed_field] = f'{payload[changed_field]}a'
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.patch(Urls.CHANGE_USER_DATA_URL, data=payload, headers=headers)
        assert response.status_code == 200
        assert response.json().get('success') is True
        assert 'user' in response.json()
        user_data = response.json()['user']
        assert 'email' in user_data
        assert 'name' in user_data

    @allure.title('Проверка неудачной попытки изменения данных пользователя без аутентификации')
    @pytest.mark.parametrize('changed_field', ['email', 'password', 'name'])
    def test_failed_user_data_change_without_authentication(self, create_user, changed_field):
        payload = {'email': create_user[1],
                   'password': TestData.TEST_USER_PASSWORD,
                   'name': TestData.TEST_USER_NAME
                   }
        payload[changed_field] = f'{payload[changed_field]}a'
        response = requests.patch(Urls.CHANGE_USER_DATA_URL, data=payload)
        assert response.status_code == 401
        assert response.json().get('success') is False
        assert response.json()['message'] == ErrorsMessages.AUTHORISED_ERROR_401
