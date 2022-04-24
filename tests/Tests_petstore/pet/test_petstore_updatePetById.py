# в фикстуре ручки разобраться с передачей нескольких параметров!
def test_getPetById(app):
    """Тест на обновление данных питомца по id"""
    petId = app.get_datas.get_someId(55, 66)
    petName = app.get_datas.get_petName()
# создание питомца для поиска его id
    app.petstore_pet.post_pet(petId, petName)
    petName2 = app.get_datas.get_petName()
    status = 'sold'
    req = app.petstore_pet.post_petId(petId, petName2, status)
    assert req.status_code == 200, f'Что-то пошло не так'
