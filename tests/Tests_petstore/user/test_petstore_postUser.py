import random

def test_createUser(app):
    """Тест на создание нового пользователя"""
    userId = random.randint(100, 200)
    userName = random.choice(['Strange', 'PetLove', 'LovePet', 'lOvEpEt', 'LooooovePet'])
    listName = ['Артем', 'Дмитрий', 'Кирилл', 'Максим', 'Илья', 'Станислав', 'Денис', 'Владимир', 'Евгений', 'Александр']
    firstName = random.choice(listName)
    lastName = 'Ланцов'
    email = 'test@user.pet'
    password = 'password'
    phone = '+79113332211'
    req = app.petstore_user.post_user(userId, userName, firstName, lastName, email, password, phone)
    assert req.status_code == 200, f'Тест на создание нового пользователя не пройден'
