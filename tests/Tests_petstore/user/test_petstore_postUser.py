
def test_createUser(app):
    """Тест на создание нового пользователя"""
    userId = app.get_datas.get_someId(99, 121)
    userName = app.get_datas.get_userName()
    firstName = app.get_datas.get_firstName()
    lastName = app.get_datas.get_secondName()
    email = app.get_datas.get_email()
    password = 'password'
    phone = app.get_datas.get_phoneNumber()
    req = app.petstore_user.post_user(userId, userName, firstName, lastName, email, password, phone)
    assert req.status_code == 200, f'Тест на создание нового пользователя не пройден'
