class Data:
    valid_login = 'Pavel1987'
    valid_password = 'qwerty'
    valid_firstname = 'Pavel'
    valid_courier_data = {'login': 'Pavel1987', 'password': 'qwerty', 'firstName': 'Pavel'}
    courier_data_without_name = {'login': 'Pavel1987', 'password': '1234'}
    courier_data_with_wrong_password = {'login': 'Pavel1987', 'password': '123456'}
    courier_with_repeating_login = {'message': 'Этот логин уже используется'}
    created_valid_courier = {'ok': True}
    not_enough_data_to_create_courier = {'message': 'Недостаточно данных для создания учетной записи'}
    login_not_found = {'message': 'Учетная запись не найдена'}
    not_enough_data_to_login = {'message': 'Недостаточно данных для входа'}

class OrderData:
    order_data_grey_1 = {
        'firstName': 'Олег',
        'lastName': 'Сопин',
        'address': 'Рабочая, 2',
        'metroStation': 8,
        'phone': '+79039999999',
        'rentTime': 3,
        'deliveryDate': '2025-05-20',
        'comment': 'Поехали',
        'color': [
            'GREY'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Сергей',
        'lastName': 'Пузанов',
        'address': 'Радужная',
        'metroStation': 10,
        'phone': '+79168888888',
        'rentTime': 7,
        'deliveryDate': '2025-05-23',
        'comment': 'Вези быстрей',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Дмитрий',
        'lastName': 'Яковлев',
        'address': 'Диверсантов, 16',
        'metroStation': 15,
        'phone': '+79097777777',
        'rentTime': 1,
        'deliveryDate': '2025-05-29',
        'comment': 'В чем сила, брат',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Андрей',
        'lastName': 'Трещалин',
        'address': 'Крюковская, 102',
        'metroStation': 20,
        'phone': '+79646666666',
        'rentTime': 2,
        'deliveryDate': '2025-05-30',
        'comment': 'Надежда глупое чувство',
        'color': []
    }