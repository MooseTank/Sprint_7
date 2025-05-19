import allure
import pytest
from data import Data
from courier_api import CourierAPI
from helpers import create_random_login, create_random_password, create_random_firstname


@allure.title("Создание курьера")
class TestCourierCreate:
    @allure.description("Успешное создание курьера")
    def test_create_courier_success(self, delete_courier):
        payload = {
            "login": create_random_login(),
            "password": create_random_password(),
            "firstName": create_random_firstname()
        }
        courier_api = CourierAPI()
        response = courier_api.create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        delete_courier(payload["login"], payload["password"])

    @allure.title('Проверка получения ошибки при повторном использовании логина для создания курьера')
    @allure.description('Проверяются код и тело ответа.')
    def test_create_courier_account_login_taken_conflict(self):
        payload = {
            'login': Data.valid_login,
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        courier_api = CourierAPI()
        response = courier_api.create_courier(payload)
        assert response.status_code == 409 and response.json() == Data.courier_with_repeating_login

    @allure.title('Проверка получения ошибки при создании курьера с незаполненными обязательными полями')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()},
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        courier_api = CourierAPI()
        response = courier_api.create_courier(empty_credentials)
        assert response.status_code == 400 and response.json() == Data.not_enough_data_to_login