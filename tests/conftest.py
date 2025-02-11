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
               'password': TestData.TEST_USER_PASSWORD,
               'name': TestData.TEST_USER_NAME
               }
    response = requests.post(Urls.REGISTER_URL, data=payload)
    access_token = response.json().get('accessToken')
    yield response, login, access_token
    headers = {'Authorization': f'{access_token}'}
    requests.delete(Urls.DELETE_USER_URL, headers=headers)
