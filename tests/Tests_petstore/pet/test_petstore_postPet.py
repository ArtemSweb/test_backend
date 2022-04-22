import random


def test_addNewPet(app):
    """Тест на создание нового питомца"""
    petId = app.get_datas.get_someId(13, 28)
    petName = app.get_datas.get_petName()
    req = app.petstore_pet.post_pet(petId, petName)
    assert req.status_code == 200, f'Тест на создание нового питомца не пройден'

