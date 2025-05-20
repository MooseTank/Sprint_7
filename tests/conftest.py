import pytest
import requests
from urls import Urls


@pytest.fixture
def delete_courier():
    login = None
    password = None

    def _delete_courier(login_, password_):
        nonlocal login, password
        login = login_
        password = password_

    yield _delete_courier

    if login and password:
        login_response = requests.post(Urls.URL_COURIER_LOGIN, data={
            "login": login,
            "password": password
        })

        if login_response.status_code == 200 and "id" in login_response.json():
            courier_id = login_response.json()["id"]
            requests.delete(f"{Urls.URL_ORDERS_CREATE}/{courier_id}")