import pytest
import requests
from urls import Urls


@pytest.fixture
def delete_courier():
    created_login = None
    created_password = None

    yield  # yield без передачи функции

    if created_login and created_password:
        login_response = requests.post(Urls.URL_COURIER_LOGIN, data={
            "login": created_login,
            "password": created_password
        })

        if login_response.status_code == 200 and "id" in login_response.json():
            courier_id = login_response.json()["id"]
            requests.delete(f"{Urls.URL_ORDERS_CREATE}/{courier_id}")

    def set_credentials(login_, password_):
        nonlocal created_login, created_password
        created_login = login_
        created_password = password_

    return set_credentials