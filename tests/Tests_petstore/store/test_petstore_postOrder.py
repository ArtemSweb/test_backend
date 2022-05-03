import random
import pytest

#разобраться почему 404
@pytest.mark.skip(reason="404")
def test_placeOrder(app):
    """Тест на создание нового заказа"""
    orderId = app.get_datas.get_someId(1, 10)
    petId = app.get_datas.get_someId(13, 28)
    quantity = random.randint(1, 3)
    status = 'placed'
    complete = "False"
    req = app.petstore_store.post_storeOrder(orderId, petId, quantity, status, complete)
    assert req.status_code == 200, f'Тест на создание нового заказа не пройден'