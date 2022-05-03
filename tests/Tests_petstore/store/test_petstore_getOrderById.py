import random

def test_getOrderById(app):
    """Тест на получение данных заказа по id"""
    orderId = random.randint(1, 6)
    req = app.petstore_store.get_storeOrderById(orderId)
    assert req.status_code == 200, f'Что-то пошло не так'