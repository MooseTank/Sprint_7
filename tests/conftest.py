import pytest
import requests
from helpers import create_random_login, create_random_password, create_random_firstname
from courier_api import CourierAPI
from urls import Urls


@pytest.fixture
def create_courier():
    # Создаем тестовые данные
    payload = {
        "login": create_random_login(),
        "password": create_random_password(),
        "firstName": create_random_firstname()
    }

    # Создаем курьера
    courier_api = CourierAPI()
    response = courier_api.create_courier(payload)

    # Сохраняем данные для последующего удаления
    created_login = payload["login"]
    created_password = payload["password"]

    # Возвращаем данные для использования в тесте
    yield response

    # Удаляем курьера после теста
    login_response = requests.post(Urls.URL_COURIER_LOGIN, data={
        "login": created_login,
        "password": created_password
    })

    if login_response.status_code == 200 and "id" in login_response.json():
        courier_id = login_response.json()["id"]
        requests.delete(f"{Urls.URL_ORDERS_CREATE}/{courier_id}")