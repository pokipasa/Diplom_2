import requests
import allure
from unittest.mock import patch

from data import Urls
from data import ErrorsMessages


class TestCreateOrder:

    @allure.title('Успешная проверка создания заказа с аутентификацией и добавленными ингредиентами')
    def test_successful_order_creation_with_auth_and_ingredients(self, create_user):
        payload = {'ingredients': ['61c0c5a71d1f82001bdaaa6c']}
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.post(Urls.create_order_url, data=payload, headers=headers)
        assert response.status_code == 200
        assert response.json().get('success') is True
        assert 'name' in response.json()
        assert 'order' in response.json()
        order_data = response.json().get('order')
        assert 'number' in order_data

    @allure.title('Проверка неудачной попытки создания заказа без аутентификации')
    @patch('requests.post')
    def test_failed_order_creation_without_auth(self, mock_post):
        mock_post.return_value.status_code = 401
        mock_post.return_value.json.return_value = {'success': False, 'message': ErrorsMessages.authorised_error_401}
        payload = {'ingredients': ['goodhash']}
        response = requests.post(Urls.create_order_url, data=payload)
        assert response.status_code == 401
        assert response.json().get('success') is False
        assert response.json()['message'] == ErrorsMessages.authorised_error_401

    @allure.title('Проверка неудачной попытки создания заказа без выбора ингредиентов')
    def test_failed_order_creation_without_ingredients(self, create_user):
        payload = {}
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.post(Urls.create_order_url, data=payload, headers=headers)
        assert response.status_code == 400
        assert response.json().get('success') is False
        assert response.json()['message'] == ErrorsMessages.create_order_error_400

    @allure.title('Проверка отказа в создании заказа с неверным хеш-кодом ингредиента')
    def test_failed_order_creation_with_invalid_ingredient_hash(self, create_user):
        payload = {'ingredients': ['wronghash']}
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.post(Urls.create_order_url, data=payload, headers=headers)
        assert response.status_code == 500
