import pytest
import requests
import random
import string

from data import Urls, TestData


@pytest.fixture
def create_user():
    letters = string.ascii_lowercase
    login = ''.join(random.choice(letters) for _ in range(10)) + '@yandex.ru'
    payload = {'email': f'{login}',
               'password': TestData.test_user_password,
               'name': TestData.test_user_name
               }
    response = requests.post(Urls.register_url, data=payload)
    access_token = response.json().get('accessToken')
    yield response, login, access_token
    headers = {'Authorization': f'{access_token}'}
    requests.delete(Urls.delete_user_url, headers=headers)
