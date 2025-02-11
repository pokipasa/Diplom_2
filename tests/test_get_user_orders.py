import requests
import allure

from data import Urls
from data import ErrorsMessages


class TestGetUserOrders:

    @allure.title('Проверка успешного получения заказов для авторизованного пользователя')
    def test_get_user_orders_with_authorization(self, create_user):
        payload = {'ingredients': ['dfbgdrselcmw5u']}
        headers = {'Authorization': f'{create_user[2]}'}
        requests.post(Urls.CREATE_ORDER_URL, data=payload, headers=headers)
        response = requests.get(Urls.GET_USER_ORDERS, headers=headers)
        assert response.status_code == 200
        assert response.json().get('success') is True

    @allure.title('Проверка неудачной попытки получения заказов для неавторизованного пользователя')
    def test_get_user_orders_without_authorization(self, create_user):
        payload = {'ingredients': ['dfbgdrselcmw5u']}
        headers = {'Authorization': f'{create_user[2]}'}
        requests.post(Urls.CREATE_ORDER_URL, data=payload, headers=headers)
        headers = {}
        response = requests.get(Urls.GET_USER_ORDERS, headers=headers)
        assert response.status_code == 401
        assert response.json().get('success') is False
        assert response.json()['message'] == ErrorsMessages.AUTHORISED_ERROR_401
