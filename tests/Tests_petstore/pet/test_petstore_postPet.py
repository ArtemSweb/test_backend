import random


def test_addNewPet(app):
    """Тест на создание нового питомца"""
    petId = random.randint(100, 200)
    listName = ['Хорос','Тяпа','Гера','Джордж','Ра']
    petName = random.choice(listName)
    req = app.petstore_pet.post_pet(petId, petName)
    assert req.status_code == 200, f'Тест на создание нового питомца не пройден'

