import random


class datasHelper:

    def __init__(self,app):
        self.app = app

    def get_firstName(self):
        listName = ('Артем', 'Дмитрий', 'Кирилл', 'Максим', 'Илья', 'Станислав', 'Денис', 'Владимир', 'Евгений', 'Александр')
        firstName = random.choice(listName)
        return firstName

    def get_secondName(self):
        listsecondName = ('Смирнов', 'Лазарев', 'Карпов', 'Сафонов', 'Шаров', 'Иванов', 'Медведев', 'Афанасьев', 'Капустин')
        secondName = random.choice(listsecondName)
        return secondName

    def get_userName(self):
        listName = ('Strange', 'PetLove', 'LovePet', 'lOvEpEt', 'LooooovePet')
        userName = random.choice(listName)
        return userName

    def get_petName(self):
        listName = ('Хорос', 'Тяпа', 'Гера', 'Джордж', 'Ра')
        petName = random.choice(listName)
        return petName

    def get_email(self):
        listfirst = ['',]
        listsecond = ('yandex', 'gmail', 'inbox', 'rambler')
        listdomain = ('ru', 'com', 'net', 'su')
        first = random.choice(listfirst)
        second = random.choice(listsecond)
        dom = random.choice(listdomain)
        return f'{first}@{second}.{dom}'

    def get_someId(self, start, end):
        someId = random.randint(start, end)
        return someId
