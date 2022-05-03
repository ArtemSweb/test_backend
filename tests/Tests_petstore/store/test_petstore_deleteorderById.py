
def test_deleteOrderById(app):
    """Удаление заказа по id"""
    orderId = '1'
    req = app.petstore_store.delete_storeOrderById(orderId)
    assert req.status_code == 200, f'Тест на удаление заказа по id не пройден'