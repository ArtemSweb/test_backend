import random

def test_getPetById(app):
    """Тест на получение информации о питомце по id"""
    petId = random.randint(100, 200)
    listName = ['Хорос','Тяпа','Гера','Джордж','Ра']
    petName = random.choice(listName)
# создание питомца для поиска его id
    newPet = app.petstore_pet.post_pet(petId, petName)
    req = app.petstore_pet.get_pet_id(petId)
    assert req.status_code == 200, f'Тест на получение данных по ID не пройден'
