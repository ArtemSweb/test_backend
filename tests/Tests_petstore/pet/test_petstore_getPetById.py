
def test_getPetById(app):
    """Тест на получение информации о питомце по id"""
    petId = app.get_datas.get_someId(55, 66)
    petName = app.get_datas.get_petName()
# создание питомца для поиска его id
    app.petstore_pet.post_pet(petId, petName)
    req = app.petstore_pet.get_petId(petId)
    assert req.status_code == 200, f'Тест на получение данных по ID не пройден'
