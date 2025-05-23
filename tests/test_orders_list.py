import allure
from courier_api import OrderAPI

class TestOrdersListGet:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверяются код и тело ответа.')
    def test_orders_list_get_success(self):
        order_api = OrderAPI()
        response = order_api.get_orders_list()
        assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]