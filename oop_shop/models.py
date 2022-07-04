class Category:
    def __init__(self, title):
        self.title = title
    def __str__(self):


class Product:
    def __init__(self, title, price, description, quantity):
        self.title = title
        self.price = price
        self.desc = description
        self.quantity = quantity
    
class Comment:
    def __init__(self, user, product, body):
        permissions.login_required(user)
        from datetime import datetime
        
        self.user = user
        self.product = product
        self.body = body


class User:
    def __init__(self, email, name, sex):
        self.email = email
        self.name = name
        self.sex = sex
        self.__password = None
        self.is_authenticated = False
        print(f'Успешно создан юзер {self.email}')

    def register(self, password, password_confirm):
        if password != password_confirm:
            raise Exception("Пароли не совпадают")
        self.__password = password
        print(f'Успешно зарегестрирован юзер {self.email}')

    def login(self, password):
        if self.__password != password:
            raise Exception("Пароль не верный")
        self.is_authenticated = True

    def logout(self):
        permissions.login_require(self)
        self.is_authenticated = False
        print(f'Успешно вошел юзер {self.email}')
    def 