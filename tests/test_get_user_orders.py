import requests
import allure

from data import Urls
from data import ErrorsMessages


class TestGetUserOrders:

    @allure.title('Проверка получения заказов авторизованным пользователем')
    def test_get_user_orders_with_authorization(self, create_user):
        payload = {'ingredients': ['dfbgdrselcmw5u']}
        headers = {'Authorization': f'{create_user[2]}'}
        requests.post(Urls.create_order_url, data=payload, headers=headers)
        response = requests.get(Urls.get_user_orders, headers=headers)
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Проверка попытки получения заказов неавторизованным пользователем')
    def test_get_user_orders_without_authorization(self, create_user):
        payload = {'ingredients': ['dfbgdrselcmw5u']}
        headers = {'Authorization': f'{create_user[2]}'}
        requests.post(Urls.create_order_url, data=payload, headers=headers)
        headers = {}
        response = requests.get(Urls.get_user_orders, headers=headers)
        assert response.status_code == 401
        assert response.json().get('success') is False
        assert response.json()['message'] == ErrorsMessages.authorised_error_401
