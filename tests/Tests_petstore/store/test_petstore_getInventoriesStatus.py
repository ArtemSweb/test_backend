
def test_getInventoryStatus(app):
    req = app.petstore_store.get_storeInventory()
    assert req.status == 200, f'Тест на получение статуса не пройден'