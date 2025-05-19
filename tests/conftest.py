import pytest
import requests
from urls import Urls

# Фикстура для удаления курьера
@pytest.fixture
def delete_courier():
    def delete_courier(login, password):
        login_response = requests.post(Urls.URL_COURIER_LOGIN, data={
            "login": login,
            "password": password
        })

        # Получаем ID курьера, если он есть
        if login_response.status_code == 200 and "id" in login_response.json():
            courier_id = login_response.json()["id"]
            requests.delete(f"{Urls.URL_ORDERS_CREATE}/{courier_id}")

    return delete_courier