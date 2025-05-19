import allure
import pytest
from data import OrderData
from courier_api import OrderAPI


class TestOrderCreate:
    @allure.title('Проверка создания заказа с разными параметрами цвета')
    @allure.description('Согласно требованиям, система должна позволять указать в заказе один цвет самоката, выбрать '
                        'сразу оба или не указывать совсем. В тест по очереди передаются наборы данных с разными '
                        'параметрами: серый, черный, оба цвета, цвет не указан. Проверяются код и тело ответа.')
    @pytest.mark.parametrize('order_data', [
        OrderData.order_data_grey_1, OrderData.order_data_black_2,
        OrderData.order_data_two_colors_3, OrderData.order_data_no_colors_4
    ])
    def test_order_crete_color_parametrize_success(self, order_data):
        order_api = OrderAPI()
        response = order_api.create_order(order_data)

        assert response.status_code == 201
        assert 'track' in response.text