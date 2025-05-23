import requests
import json
from urls import Urls

class CourierAPI:
    def create_courier(self, payload):
        response = requests.post(Urls.URL_COURIER_CREATE, data=payload)
        return response

    def courier_login(self, credentials):
        response = requests.post(Urls.URL_COURIER_LOGIN, data=credentials)
        return response


class OrderAPI:
    def create_order(self, payload, headers=None, timeout=5):
        if headers is None:
            headers = {'Content-Type': 'application/json'}
        response = requests.post(
            Urls.URL_ORDERS_CREATE,
            data=json.dumps(payload),
            headers=headers,
            timeout=timeout
        )
        return response

    def get_orders_list(self):
        response = requests.get(Urls.URL_ORDERS_CREATE)
        return response