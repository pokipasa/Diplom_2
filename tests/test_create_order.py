import requests
import allure
from unittest.mock import patch

from data import Urls
from data import ErrorsMessages


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа с авторизацией и ингредиентами')
    def test_create_order_with_authorization_and_ingredients(self, create_user):
        payload = {'ingredients': ['61c0c5a71d1f82001bdaaa6c']}
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.post(Urls.create_order_url, data=payload, headers=headers)
        assert response.status_code == 200
        assert response.json().get('success') is True
        assert 'name' in response.json()
        assert 'order' in response.json()
        order_data = response.json().get('order')
        assert 'number' in order_data


    @allure.title('Проверка попытки создания заказа без авторизации')
    @patch('requests.post')
    def test_create_order_without_authorization(self, mock_post):
        mock_post.return_value.status_code = 401
        mock_post.return_value.json.return_value = {'success': False, 'message': EM.authorised_error_401}
        payload = {'ingredients': ['61c0c5a71d1f82001bdaaa6c']}
        response = requests.post(Urls.create_order_url, data=payload)
        assert response.status_code == 401
        assert response.json().get('success') is False
        assert response.json()['message'] == EM.authorised_error_401


    @allure.title('Проверка попытки создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self, create_user):
        payload = {}
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.post(Urls.create_order_url, data=payload, headers=headers)
        assert response.status_code == 400
        assert response.json().get('success') is False
        assert response.json()['message'] == ErrorsMessages.create_order_error_400


    @allure.title('Проверка неудачной попытки создания заказа с неправильным хешем ингредиента')
    def test_order_creation_with_wrong_ingredients_hash_failed(self, create_user):
        payload = {'ingredients': ['wronghash']}
        headers = {'Authorization': f'{create_user[2]}'}
        response = requests.post(Urls.create_order_url, data=payload, headers=headers)
        assert response.status_code == 500