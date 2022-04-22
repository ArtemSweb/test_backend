

def test_getPetById(app):
    petId = '1'
    req = app.petstore_pet.get_pet_id(petId)
    assert req.status_code == 200, f'Тест на получение данных по ID не пройден'
