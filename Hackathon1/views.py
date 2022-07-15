from models import Cars 
from pprint import pprint
from decimal import Decimal
def cars_create():
    body_types = ['Седан', 'Универсал', 'Купе', 'Хэтчбек', 'Минивен', 'Внедорожник', 'Пикап']
    brand = input('Введите название авто: ')
    model = input('Введите название модели авто: ')
    year = int(input('Введите год выпуска авто: '))
    volume = Decimal(input('Введите обьем двигателя авто: '))
    volume = volume.quantize(Decimal("1.0"))
    color = input('Выберите цвет авто: ')
    print("Выберите тип кузова авто: ")
    for type in body_types:
        print(f'*{type}')
    body_t = input('********************\n Выберите тип кузова из предложенных вариантов: ')
    milleage = int(input('Введите пробег авто:  '))
    price = Decimal(input('Введите цену авто:  '))
    price = price.quantize(Decimal("1.00"))

    Cars(brand, model, year, volume, color, kuzov, milleage, price)
    return 'Авто успешно создано'

def cars_listing():
    fields = ['Марка', 'Модель', 'Год выпуска', 'Цвет', 'Типы кузовов', 'Пробег', 'Стоимость']
    list_ = []
    for car in Cars.objects:
        list_.append({'Марка':car.mark, 'Модель':car.model, 'Год выпуска':car.year, 'Объем':car.volume, 'Цвет':car.color, 'Тип кузовов':car.type_, 'Пробег':car.prob, 'Стоимость':car.price})
    pprint(list_)

def cars_retrieve(_id):
    list_ = []
    for car in Cars.objects:
        list_.append({'Марка':str(car.mark), 'Модель':str(car.model), 'Год выпуска':str(car.year), 'Объем двигателя':str(car.volume), 'Цвет':str(car.color), 'Тип кузова':str(car.type_), 'Пробег авто':str(car.prob), 'Стоимость':str(car.price)})
    print(list_[_id])

def cars_update(_id):
    car = Cars.objects[_id]
    field = input("Что вы желаете изменить из предложенных вариантов: (mark, model, year, volume, color, type_, prob, price): ")
    if field in dir(car):
        print(f"old value: {getattr(car, field)}")
        value = input(f"{field} = ")
        if field == 'type_':
            if value not in Cars.type_kuz:
                raise Exception(f'Введите верный тип! {Cars.type_kuz}')
        setattr(car, field, value)
    else:
        raise Exception(f"Поля {field} не cуществует!")
    cars_listing()
    list_ = []
    for car in Cars.objects:
        list_.append({'Марка':str(car.mark), 'Модель':str(car.model), 'Год выпуска':str(car.year), 'Объем двигателя':str(car.volume), 'Цвет':str(car.color), 'Тип кузова':str(car.type_), 'Пробег авто':str(car.prob), 'Стоимость':str(car.price)})

def cars_delete(_id):
    car = Cars.objects[_id]
    Cars.objects.remove(car)
    print('Авто успешно удалено!')
    cars_listing()