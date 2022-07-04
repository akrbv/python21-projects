"""
Создайте список list_ из целых чисел от 1 до 100 (включительно). Нужно использовать comprehension.
"""

set_ = {False, 2, 3, 4, 4, 4, 1, 0}

print(sorted(set_))
list_ = {i:i for i in range(1, 101)}





dict_ = {1: 'hello', 2: {123: 'asdasd', 'bootcamp': 4}, 234: 234, 3: 'bootcamp'}
res = {
    key if type(key) == int else val
    : 
    {val2: key2 for key2, val2 in val.items()} if type(val) == dict else val
    for key, val in dict_.items()
}
print(res)



# for key in dict_.items():
#     print(key)
# list_2 = []
# for i in range(1, 101):
#     list_2.append(i)

# print(list_2)



# import string

# for i in range(10):
#     if i != 3:
#         print(i)
# i = 1
# while i < len(string.ascii_uppercase):
#     print(string.ascii_uppercase[i])
#     i += 2




"""
Дан вложенный словарь dict_ (словарь состоящий из других словарей) в котором ключом является имя студента, а значением словарь с его оценками по 3 предметам.

Распечатайте новый словарь, где вместо оценкок будет название предмета, по которому студент имеет высший балл. Нужно использовать comprehension.

{'Timur': 'math', 'Olga': 'math', 'Nik': 'literature'}
"""

# dict_ = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
#     'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
# }
# res2 = {}

# """
# Solution with comprehension
# """
# res = {key1: key2 for key1, val1 in dict_.items() for key2, val2 in val1.items() if key2 == max(val1, key=val1.get)}


# """
# Solution with for loops
# """

# for key1, val1 in dict_.items():
#     for key2, val2 in val1.items():
#         if max(val1.values()) == val2:
#             res2[key1] = key2

# # res = max(['hello', 'makers', 'bootcamp'])
# # val1.values() = [90, 95, 91]
# print(res)
# print(res2)

"""
Mutable - set, dictionary, list
Immutable - str, int, bool, float
"""

# str_ = 'makers'
# list_ = [1, 2, 3]

print()
# list_.pop()
# print(list_)
# str_[0] = 'm'
# print(str_)



list_ = [1, 5, 3, 2]

for num in list_:
    if list_.count(num) != 1:
        print('yes')
        break
else:
    print('no')



# dict_ = {}

# for num in list_:
#     dict_[num] = list_.count(num)

# for i in dict_.values():
#     if i != 1:
#         print('yes')
#         break
# else:
#     print('no')











самостоятельный разбор

строки

имя\n - перенос на новую строку
имя/n/n - отступ и перенос, пример с Dear, friend, пустая строка
тройные кавычки, то же самое, делает отступы
слово/n/t' - перенос и табуляция по горизонтале 
слово\v - перенос по вертикале

# сырые строки

символ r'
прмиер с url


Конкатенация
сложение строк
string1 = 'Makers'
string2 = "Bootcamp"
print('I stude at ' + string1 + ' ' + string2)



функция len() в скобачках строках
string = 'Makers Bootcamp'
print(len(string)) #пробелы тоже считаются

так же можно сразу писать в строку 
lenght = len('John')
print(lenght)


индекс
если нам нужно получить индекс, то мы обращаемся по скобкам []
пример
sentence = 'Strings are ordered'
print(sentence[18]) 
выйдет буква "d"


Срезы
прописываются по скобкам []
[x:y], где x начало среза, y конец среза
пример
string = 'Makers Bootcamp'
print(string[:3])
выйдет Mak
print(string[2:-2]) сам -2 не входит в строку
выйдет kers Bootca


Шаги
string = 'Makers Bootcamp'
print(string[::-1])
выйдет pmactooB srekaM


word = 'dream'
word = 'c' + word[1:]
print(word)
выйдет cream


Основные методы строк
№1 
find()
string = 'Makers Bootcamp'
все методы объявляются через точку, пример 'string.find'
string.find('boot')
print(string.find('boot'))
выйдет "7" индекс первого вхождения
чтобы найти индекс последнего вхождения, то добавляем r, пример  
print(string.rfind('Makers'))
выйдет 0


№2
index()
такой же как и find

№3
replace()
string = 'Makers Bootcamp'
print(string.replace("camp", "rock")) то есть происходит замена
выйдет Makers Bootrock

№4
split()
string = 'Makers Bootcamp'
string.split() - в скобачках (пустые) это список, то есть он превращается в список
['Makers', 'Bootcamp']


допустим пользователь вводит данные
full_name = input('Enter name and lastname: ')
print(full_name) выйдет просто John Snow

Метод split сплитует строку, пример 
full_name = input('Enter name and lastname: ').split()
print(full_name) выйдет ['John', 'Snow'] - превратился в тип данных список


№5
isdigit(), isalpha(), isalnum(), islower(), isupper(), isspace(), istitle()
все методы, которые заканчиваются на is возвращают булевое значение
True и False

isdigit - отвечает состоит ли строка только из чисел или нет
isalpha - так же как и isdigit только проверяет состоит ли строка из букв
isalnum - проверяет состоит ли строка из букв и цифр
islower - проверяет состоит ли строка из маленьких букв
isupper - проверяет состоит ли строка из заглавных букв
isspace - проверяет состоит ли строка из неотбражаемых символов
istitle - проверяет начинается ли слово (каждое) из строки с заглавной буквы
пример 
string = 'Makers'
print(string.isdigit())
выйдет False

№6
upper(), lower()
они преобразуют строку в большие или маленьки буквы
upper - большие
lower - маленькие

№7
startswith(), endswith()
startswith - проверяет начинается ли строка с определенной буквы или знака
endswith - проверяет заканчивается ли строка с определенной буквы или знака
пример 
string = 'Makers'
print(string.startswith('makers'))
выйдет False

№8
join()
list_ = ('makers bootcamp')
print('*'.join(list_))
выйдет m*a*k*e*r*s* *b*o*o*t*c*a*m*p
работает только со строками

№9
capitalize(), title()
capitalize - переводит первое слово в строке в верхний регистр
title - переводит каждое слово в строке в верхний регистр

пример:
string = 'bootcamp makers'
print(string.capitalize())
выйдет Bootcamp makers
print(string.title())
выйдет Bootcamp Makers


№10
count()
подсчитывает какое кол-во раз используется буква в строке

пример
string = 'bootcamp makers'
print(string.count('a'))
выйдет 2

№10
lstrip(),rstrip(), strip()
они отвечают за удаление пробельных символов
lstrip - удаляют первые символы 
strip - удаляют последние символы

пример
string = '    makers'
print(string.lstrip())
выйдет makers без начальных пробелов

№11
partition(patter)
он возвращает нам кортеж, который содержит шаблон

пример
string = 'Hello lovely Makers Bootcamp'
print(string.partition('Makers'))

выйдет ('Hello lovely ', 'Makers', ' Bootcamp')

№12

swapcase()
он переводит символы верхнего регистра в нижний и наоборот

пример 
string = ('CamelCase')
print(string.swapcase())
выйдет cAMELcASE

№13

zfill(width) - в скобачках вставить число 
этот метод заполняет первые символы нулями

пример
string = ('makers')
print(string.zfill(15))
выйдет 000000000makers

№14

ljust(width, fullchar), rjust(width, fullchar) - в скобачках вставить число и символ

пример
string = ('makers')
print(string.ljust(9, '*'))
выйдет makers***


№15

Форматирование строк
format()

#1. % - присоединяет слово к тому, что ввел пользователь

name = input()
last_name = input()
age = int(input())
some_variable = 'Welcome, %s %s, age %d' % (name, last_name, age)
print(some_variable)
выйдет Emily Klark, 15


Есть аналогичный метод
format

пример 
name = input()
last_name = input()
age = int(input())
some_variable = 'Welcome, {}, {}'.format(name, last_name, age)
print(some_variable)
выйдет 
Welcome, kate, Midlton
Your age is 25


И самый крутой метод Форматирования
f

пример
name = input()
last_name = input()
age = int(input())
some_variable = f'Welcome, {name}, {last_name}\nYour age is {age}'
print(some_variable)





функции

round - округляет числа
// - целочисленное деление когда не нужно округление
% - остаток от деления

abs - модуль числа - всегда возвращает положительное число
divmod (x. y) - x // y. x % y пример divmod(11,4)

** - возведение в степень, пример 2**2 = 4
pow(x,y,z) возводит в степень, далее делит

math.pi - вызвать число pi(пи)

bin - 2-ричная система
hex - 16-ричная система
oct - 8-ричная система

decimal - выводит точное число



Логические операторы
and и or

and - чтобы получить True при использовании оператора and, необходимо, чтобы 
результаты обоих простых выражений, которые связывают данный оператор, были истинными

or - или
тут хотя-бы один должен быть истинным 

not - превращает правду в ложь и ложь в правду, данный оператор нужно помещать
в скобки
пример if not (a > b or b > c) если мы уберем скобки, то будет работать только на 
первое выражение


if - логическое выражение:
    выражение_1
выражение_2

else - иначе (если первое условие не выполняется, то вып-ся else)
elif - когда исп- ся больше 3-х функций

пример 
list_ = [11, 20, 25, 30]
if (not 20 in list_ and 12 in list_):
    print("yes")



None - успех действий


ord - смотреть код по юни коду
к примеру print(ord(b)) - порядковое значение 98

chr() - выполняет обратное значение ord
к примеру print(chr(98)) получим b



Тернарный оператор - упрощенный вариант

пример
a = 'MAKERS'
b = 10
print(a if b > 0 else "makers")

Альтернативный способ тернарного оператора

(expression_false, expression_true)[condition] в круглых скобках кортеж
в квадратных нах-ся условие


a = 10
print(('negative','positive')[a >= 0])
выйдет positive, так как 10 больше 0


NoneType



СПИСКИ []
обозначаются в квадратных скобках []

метод append() - добавляет в список значение в конец списка
пример:
list = ['hello', 'makers', 5]
list.append(7)
print(list)
выйдет ['hello', 'makers', 5, 7]

метод pop() - удаляет значение по индексу

пример:
list = ['hello', 'makers', 5]
list.pop(2)
print(list)
выйдет ['hello', 'makers']

метод remove() - удаляет значение по слову (если не знаем индекс)

пример
list = ['hello', 'makers', 5]
list.remove('hello')
print(list)
выйдет ['makers', 5]

ЦИКЛЫ
for и while

for i in итерируемый объект
пример 
my_list = [5, 10, 15, 20, 30]
for i in my_list:
    print(my_list)
выйдет [5, 10, 15, 20, 30]
[5, 10, 15, 20, 30]
[5, 10, 15, 20, 30]
[5, 10, 15, 20, 30]
[5, 10, 15, 20, 30]

функция range - диапазон - генерирует числа
пример 
list(range(5)) - не включает число (end)
выйдет [0, 1, 2, 3, 4]

list(range(1, 5)) - генерирует числа от 1 до 4 включительно (start, end)
выйдет [1, 2, 3, 4]

list(range(1, 5, 2)) - третье число это шаг (start, end, step)
выйдет [1, 3]

numbers[] - мы создали список

Если нам нужно создать список с одним элементом
пример 
numbers[7] * 6
выйдет [7, 7, 7, 7, 7, 7, 7]


for i in range(1, 10): #-> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(i**2) - это мы возвели в степень 2
выйдет
1
4
9
16
25
36
49
64
81

Если мы хотим вывести какой-то элемент, то вызываем его по индексу
пример
print(numbers[2])

Если мы хотим изменить один элемент из списка
пример
numbers = [1, True, 'Makers', 'hello', 8.9]
numbers[3] = 'Bootcamp'
print(numbers) выйдет [1, True, 'Makers', 'Bootcamp', 8.9]

пример с циклом for i in

users = ['Tom', 'Kate', 'Lola']
for user in users:
    print(user)
выйдет:
Tom
Kate
Lola

Если мы хотим каждого поприветствовать, то будет
пример
users = ['Tom', 'Kate', 'Lola']
for user in users:
    print(f'Hello' {user})
выйдет
Hello Tom
Hello Kate
Hello Lola

Еще один пример - мы хотим чтобы все буквы были заглавными
for i in 'Makers':
    print(i.upper())
выйдет: 
M
A
K
E
R
S


МЕТОДЫ СПИСКОВ

метод append() - добавляет в список значение в конец списка
пример:
list = ['hello', 'makers', 5]
list.append(7)
print(list)
выйдет ['hello', 'makers', 5, 7]


Классный пример с приглашением гостей

guests = []
list_length = int(input('Enter number of guests: '))

for i in range(list_length):
    guest = input('Enter guest name: ')
    guests.append(guest)

print(guests)



МЕТОД extend(list) - добавляет список, расширяет список
users1 = ['Alice', 'Sam']
users2 = ['Tom', 'Red']
users1.extend(users2)
print(users1)

выйдет ['Alice', 'Sam', 'Tom', 'Red']


МЕТОД insert(index, element) - добавляет в список объект между объектами
пример

users = ['Lolo', 'Pepa', 'Tom', 'Anna']
users.insert(1, 'Kate') - то есть мы добавили 'Kate' после 1 элемента
print(users)
выйдет ['Lolo', 'Kate', 'Pepa', 'Tom', 'Anna']


МЕТОД remove(element)

пример
users = ['Tom', 'Alex', 'Fox', 'Lili']
if 'Alex' in users:
    users.remove('Alex')
else: 
    pass
print(users)



МЕТОД clear() - очищает все элементы из списка, но сам список как объект сохраняет в памяти
МЕТОД del удаляет полностью объект


МЕТОД index(element) - возвращает индекс элемента, ищет элемент по индексу

пример 
my_list = ['hello', 'makers', True, 6]
print(my_list.index('makers'))


МЕТОД count(element) - не изменяет список, просто показывает какое кол-во раз 
добавлен объект

пример
numbers = [5, 6, 7, 6, 2, 6]
print(numbers.count(6))
выйдет 6

МЕТОД sort() - сортирует возростанию, строки сортирует в алфавитном порядке

пример
users = ['Tom', 'Alex', 'Fox', 'Lili']
users.sort()
print(users)
выйдет ['Alex', 'Fox', 'Lili', 'Tom']

Так же есть еще такой метод как key
пример
users = ['Tom', 'Alex', 'Fox', 'Lili']
users.sort(key=len) - сортирует по длине 
print(users)
выйдет ['Tom', 'Fox', 'Alex', 'Lili']


МЕТОД reverse() - переворачивает список в обратный порядок
пример
users = ['Tom', 'Alex', 'Fox', 'Lili']
users.reverse()
print(users) 
выйдет ['Lili', 'Fox', 'Alex', 'Tom']

МЕТОД copy() - создаёт копию списка
пример
users1 = ['Tom', 'Alex', 'Fox']
users2 = users1.copy()
print(users2)
выйдет ['Tom', 'Alex', 'Fox']



ФУНКЦИИ

len() - возвращает длину списка
пример 
numbers = [1, 2, 3, 4, 5, 6, 7]
print(len(numbers))
выйдет 7 

ФУНКЦИЯ max(), min() - выводит максимальный или минимальный элемент их списка

ФУНКЦИЯ sum() - выводит общую сумму списка

ФУНКЦИЯ sorted() - не изменяет объект, сортирует, если хотим просто отсортировать список
пример 
numbers = [1, 2, 3, 4, 5, 6, 7]



СРЕЗЫ

пример
my_list = [1, 2, 3, 4, 5]
# list[x:y] - где x - начало среза, y - конец среза
my_list = my_list[1:4]
print(my_list)
выйдет [2, 3, 4]

Так же, можем обозначить шаг, то есть будет [x:y:z]
пример 
my_list = [1, 2, 3, 4, 5]
my_list = my_list[1:4:2]
print(my_list)
выйдет [2, 4]


Обращаться к элементам вложенных списков (получить элемент)

пример
users = [
    ['Tom', 23],
    ['Bob', 52],
    ['Kate',35]
]
print(users[0])
выйдет ['Tom', 23]

Если мы хотим получить только имя 'Tom', то в этом случае 

print(users[0][0])
выйдет Tom

Если мы хотим получить элемент строки из имени 'Tom', только букву 'o' 
то в этом случае
print(users[0][0][1])
выйдет o


Как создать таблицу

пример
users = [
    ['Tom', 23],
    ['Bob', 52],
    ['Kat',35]
]
for list_ in users:
    for element in list_:
        print(element,end= ' | ')
    print()
выйдет
Tom | 23 | 
Bob | 52 | 
Kat | 35 | 






labels = ['Honda', 'Kawasaki']
for i in labels:
  like = f'I like brand {i}'
  print(like)
выйдет I like brand Honda
I like brand Kawasaki





СЛОВАРИ
создать словарь можно так:
dict_= {}
print(dict_)
my_dict = {'name': 'Sam'}

Есть Альтернативный способ создания словаря
my_dict = dict(a=1, b=2, c=3)

Можем посмотреть элемент по ключу

пример
dict_ = {'Tom': 'black',
'Alice': 'red',
'Dima': 'green'}
print(dict_['Tom'])

выйдет black

Как изменить определенной элемент

пример
dict_ = {'Tom': 'black',
'Alice': 'red',
'Dima': 'green'}
dict_ ['Tom'] = 'blue'
print(dict_)

выйдет {'Tom': 'blue', 'Alice': 'red', 'Dima': 'green'}

Мы так же, можем на ходу создать новую пару ключа и значения

пример
dict_ ['Andrey'] = 'pink'

МЕТОДЫ СЛОВАРЕЙ 

get(key, None) - получения значения
пример
my_dict = {1: 'Tom', 2:'lola', 3:'Kate'}
print(my_dict.get(1))
выйдет Tom


МЕТОД clear() - очищает словарь
пример
my_dict = {1: 'Tom', 2:'lola', 3:'Kate'}
my_dict.clear()
print(my_dict)
выйдет {}


МЕТОД copy() - создает копию словаря

МЕТОД pop(key, default) - удаляет ключ:значение
пример
dict_ = {'name': 'Kate', 'height': 170, 'weight': 50}
print(dict_.pop('weight')) - возвращает удаленное значение 
print(dict_ )
выйдет {'name': 'Kate', 'height': 170}


МЕТОД popitem() - он может удалить рандомно ключ и значение
начиная с версии 3.6 он удаляет последний элемент

МЕТОД setdefault(key, default) - возвращает значение ключа, 
так же создает ключ с каким-то значением

пример
dict_ = dict(a=1, b=2, c=3)
print(dict_.setdefault('d',5))
print(dict_)
выйдет {'a': 1, 'b': 2, 'c': 3, 'd': 5}


МЕТОД update() - объединяет 2 словаря, если в словарях есть 2 уни ключа,
то они не меняются, а значения меняются

пример
dict1 = {1:'Tom', 2:'Alice'}
dict2 = {3: 'Lola', 4: 'Kate'}
dict1.update(dict2)
print(dict1)
выйдет {1: 'Tom', 2: 'Alice', 3: 'Lola', 4: 'Kate'}


МЕТОД fromkeys(seq, value) seq - это последовательность

пример
numbers = [1, 2, 3, 4, 5]
new_dict = dict.fromkeys(numbers,"Makers")
print(new_dict)
выйдет 1: {'Makers', 2: 'Makers', 3: 'Makers', 4: 'Makers', 5: 'Makers'}


ПЕРЕБОРЫ ЭЛЕМЕНТОВ СЛОВАРЯ - items(), keys(), values()

items() - возвращает нам что-то на подобие списка, внутри которых кортежи
с ключом и значением 

пример
dict_ = {'name': 'Kate', 'height': 170, 'weight': 50}
print(dict_.items())
выйдет dict_items([('name', 'Kate'), ('height', 170), ('weight', 50)])


keys() - получить только ключи, возвращает подобие списка
values() - получить только значения, возвращает подобие списка



contacts = {
    'Alice': '+996500732632',
    'Mira': '+996557000345',
    'Nik': '+996550845696'
}
for info in contacts:
    print(info)
выйдет 
Alice
Mira
Nik

Если хотим получить ключ и значение, то применяем метод .items()
пример 
contacts = {
    'Alice': '+996500732632',
    'Mira': '+996557000345',
    'Nik': '+996550845696'
}
for key, val in contacts.items():
    print(key, val)
выйдет 
('Alice', '+996500732632')
('Mira', '+996557000345')
('Nik', '+996550845696')


поинтересней
for key, val in contacts.items():
    print(f'Name: {key}, tel: {val}')


Вложенные словари - можем посмотреть вложенные словари по значениям

nested_dictionary = {
    'Makers': {
        'Aikol': 23,
        'Rahat': 27,
        'Lola': 21
    }
}
print(nested_dictionary['Makers']['Lola'])

выйдет 21



comprehension - с помощью которой можно по опр. правилам создавать списки и СЛОВАРИ


list comprehension

пример:
my_list2 = [i for i in range(50)]
print(my_list2)

my_list2 = [i for i in range(50) if i % 2 ==0]
print(my_list2)


dictionary comprehension

пример поменяли ключ и значение 

my_dictionary = {1:'a', 2: 'b', 3: 'c'}
my_dictionary = {val: key for key, val in my_dictionary.items()}
выйдет {'a': 1, 'b': 2, 'c': 3}


Цикл for 
list_ = []
for num in range(1,21):
    list_.append(num * 2)

print(list_)
выйдет [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]


такой же, но через list comprehension
пример
list_ = [num*2 for num range(2,21)]
print(list_)

выделяем 3 части: 
num*2 - что делаем с объектом
for что мы берем
range откуда берем


Еще один пример с приглашением 

list_users = ['Alice', 'Mike', 'Ben', 'Ken', 'Adam']
invitations = ['You are invited ' + name for name in list_users]
print(invitations)
выйдет ['You are invited Alice', 'You are invited Mike', 'You are invited Ben', 'You are invited Ken', 'You are invited Adam']


Еще один пример на проверку делятся ли числа на 2 без остатка

list1 = [10, 5, -6, -8, -12, 20, 3, 14, 4]
list2 = [num for num in list1 if num % 2 == 0]
print(list2)
выйдет [10, -6, -8, -12, 20, 14, 4]

Так же можно добавить and или or
пример
list2 = [num for num in list1 if num % 2 == 0 or num % 3 == 0]


пример со строками, тип только числа, чтобы были

strings = ['1998', '2001г', '2008год', '2020']
list_ = [year for year in strings if year.isdigit()]
print(list_)
выйдет ['1998', '2020']


Пример с длинами имен

list_ = ['Tosya', 'Lola', 'Sam', 'Pollina']
list_ = [len(name) for name in list_]
print(list_)
выйдет [5, 4, 3, 7]


пример с if и else 
list_ = -[5, -12, 0, 1, 2, 8, 4, 15, 7]
list_ = [x if x < 0 else x ** 2 for x in list_]
x оставляем в таком же виде, если x будет меньше 0, в противном случае x возвести в куб
берем из list_
print(list_)
выйдет [-5, -12, 0, 1, 4, 64, 16, 225, 49]
так же сюда можем добавить фильтр             # делится без остатка
list_ = [x if x < 0 else x ** 2 for x in list_ if x % 2 == 0]


пример с именами, сложный

list_users = ['Alice', 'Mike', 'Ben', 'Ken', 'Adam' 'pop123', 'tyueoc1', 'grriihdee']
filtered_names = [x + 'MAKERS' if len(x) >= 5 else x + 'makers' for x in list_users if x.isalpha()]
print(filtered_names)
выйдет ['AliceMAKERS', 'Mikemakers', 'Benmakers', 'Kenmakers', 'grriihdeeMAKERS']


пример с процентами

John = {'name': 'John', 'age': 22}
Raychel = {'name': 'Raychel', 'age': 23}
Peter = {'name': 'Peter', 'age': 17}

users = [John, Raychel, Peter]

ages = [user.get('age', None) for user in users]

bigger = 0
smaller = 0
count = 0

for age in ages:
    if age >= 18:
        bigger += 1
    else:
        smaller += 1
    count += 1
bigger = bigger * (100/count)
bigger = smaller * (100/count)
print(f'Процент пользователей с возрастом больше 18: {round(bigger)}')
print(f'Процент пользователей с возрастом меньше 18: {round(smaller)}')



пример с матрицей
matrix = [
  [0, 2, 5, 6],
  [7,3, 0, 7],
[5, 7, 1, 6] ]
ucompress = [n for row in matrix for n in row]
print(ucompress)
выйдет [0, 2, 5, 6, 7, 3, 0, 7, 5, 7, 1, 6]

пример со временем

list_ [i for i in range(100000)]
print(datetime.now() - start)


Try-except

try: #сбор данных
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    result = num1 / num2
except ZeroDivisionError: #на случай, если юзер ввел 0
    print('На ноль делить нельзя')
except ValueError: #на случай, если юзер ввел строку\букву
    print('Вы ввели не число')
else: #если всё правильно
    print(result)
finally: #по-любому выходит(во всех случаях)
    print('Программа завершена')

while True - бесконечный цикл


list_ = [i for i in range(1,31)]
print(list_)


except Exception as e - ловит ошибки

оператор raise

number = int(input('Введите число от 1 до 50: '))
if not number in range(1, 51):
    raise Exception('Вы ввели число, которое не находится в данном промежутке')
print ('okey')




функции
как вызвать функцию
def name_of_function():
    some_code
    return variable

name_of_function()




#определение функции
def double():
    number = int(input('Enter number: '))
    print(number * 2)
    return number * 2
# вызов функции
double()

def add(a,b):
    result = a + b
    print(result)
    return(result)

add(num1, num2)


def Welcome(name, last_name):
    return f'Welcome, {name} {last_name}'

name = input()
last_name = input()

print(welcome(name, last_name))
   


пример с двумия функциями
def get_word(word):
    list_letters = list(word)
    return list_letters

def get_vowels(letter):
    vowels = ['a', 'o', 'y', 'i', 'e', 'u']
    list_vowels = [letter for letter in letter if letter in vowels]
    result = ''.join(list_vowels)
    return result

my_word = input('Enter the word: ')
print(get_vowels(get_word(my_word)))




ФУНКЦИИ - очень полезный инструмент, который позволяет многократно вызывать один и тот же код из 
разных мест программы, не нарушая принцип DRY
Если мы передаем при вызове функции конкретные значения - то мы уже работаем с аргументами.


ФУНКЦИИ
def name_of_function(): #название фунции может быть любое. В скобках могут быть параметры
    some_code
    return variable

если мы хотим вызвать функцию, то ставим
name_of_function()

Пример вызова функции:
def double():
    number = int(input('Enter number: '))
    print(number *2)
    return number *2
# вызов функции
double()


Параметры:
Параметры представляют собой локальные переменные, которым присваиваются значения в момент 
вызова функции. Конкретные значения, которые передаются в функции при её вызове, называются
аргументами.
--------------------------------------------
num1 = 63
num2 = 7

def add(a, b): 
    result = a+b
    print(result)
    return result
add(num1, num2)
--------------------------------------------



def summa_chisel():
    num1 = int(input('enter 1 num: '))
    num2 = int(input('enter 2 num: '))
    print(num1 + num2)
summa_chisel()



ПРИМЕР 
def function():
    print('The function is called')
    return('Makers')
function() - внутрь ничего не передаем, так как функция не принимает никаких параметров


ПРИМЕР №2
def substract():
    num1 = 20
    num2 = 5
    print(num1 + num2)
    return num1 - num2

substract() #если substract поместить в функцию print, то мы увидим, что нам вернул return
#если мы уберем print, то она нам покажет, что запринтила наша функция, но не покажет, что возвратила

return  - это ключевое слово, это что возвращает нам функция
print - не возвращает результат

Функции можно присваивать переменные 
пример:
variable = substract()
print(variable)

Функцию можно передавать в структуру данных
такие как:
# списки\лист, тюпл, сет, словари

пример со списком

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, substract()]


def substract():
    num1 = 20
    num2 = 5
    print(num1 + num2)
    return num1 - num2
def function():
    print('i am calling substract function')
    variable = substract()
    return variable
print(function())
#чтобы посмотреть, что нам показывает функция substract, нам нужно ее принтануть
# выйдет: i am calling substract function
# 25
# 15
# None - без print выйдет без None - она возвращает нам функцию function


ПАРАМЕТРЫ И АРГУМЕНТЫ
Функция принимает параметры(какие-то данные) с которыми мы проделываем действия,
которые прописаны внутри функции

def multiply(a, b):  #значения в скобках принимает данные
    return a * b #вернем результат умножения этих чисел

print(multiply(5, 6))  #первый аргумент 5, второй аргумент 6
#выйдет 30

можно так же передавать переменные
num1 = 70
num2 = 10
print(multiply(num1, num2))


ПРИМЕР с именами
def welcome(name, last_name):
    return f'Welcome, {name} {last_name}'
name = input()
last_name = input()
print(welcome(name, last_name))


ПРИМЕР С УБЕРИ ГЛАСНЫЕ

def get_word(word):
    list_letters = list(word) 
    return list_letters

def get_vowels(letters):
    vowels = ['a', 'o', 'y', 'i', 'e', 'u']
    list_vowels = [letter for letter in letters if letter in vowels]
    result = ''.join(list_vowels)
    return result
my_word = input('Enter the word: ')
print(get_vowels(get_word(my_word)))


Пример 2
def test_func(n1, n2=9):
    return n1 + n2
print(test_func(n1=10))

Пример 3 - можем убрать или перезаписать значения

def create_profile(name, age, image = 'default.jpg'):
    return name, age, image

print(create_profile(name = 'Tosya', age = 15))


# *args, **kwargs - они явл-ся дополнительными параметрами, которые передавать необязательно

*args - создаёт множество позиционных аргументов (передаются в кортежи)
**kwargs - создаёт словарь с именованными аргументами (передаются в словари)


def func(required, *args, **kwargs):
    print(required)

    if args: 
        print(args)
    if kwargs:
        print(kwargs)
func('Makers', 'bootcamp', 'Python', name ='Raychel', age = 89)



ФУНКЦИЯ, которая будет принимать строку. Функция должна возвращать длину этой строки.
def get_string_length(string):
    length = len(string)
    return length


ФУНКЦИЯ, которая будет принимать строку. 
принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
def get_type(arg1, arg2): #в скобках это параметры
    print(type(arg1))
    print(type(arg2))

get_type('w', 3) #в скобках это аргументы


ФУНКЦИЯ, которая распечатывает все ключи в словаре
dict_ = {'q': 2, 123: 3}

def dictionary(arg=dict_):
    for key in arg:
        print(key)

dictionary()

ФУНКЦИЯ, которая принимает переменную num в качестве аргумента и возвращает 
"It is odd number", если это число нечетное и "It is even number" если переданное число четное.

num = 6
def check(num):
    if num % 2 == 0:
        return 'It is even number'
    else:
        return 'It is odd number'

print(check(num))


ФУНКЦИЯ, которая принимает от пользователя два числа. 
Она должна сравнить эти числа между собой и вернуть максимальное значение.
def max_num(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(max_num(1,2))


Области видимости и пространства имён.

Существует 4 типа пространства имён.
1) Built-in #Встроенное пространство. Все видимые типа int, str, dir
2) Global #Глобальное пространство. Создаётся сразу при запуске тела программы
Пример:
name1 = 'makers' #глобальное пространство
name2 = 'bootcamp'

3) Enclosed #Замкнутое пространство
4) Local #Локальное пространство

Питон видит функции изнутри с local до Built-in (LEGB)

word = 'I am global'

def func_():
    word = 'I am local'
    print(word)
func_()







































'========================================================='

РАЗБОР
list_ = [1, 2, 3, 4, 5, 6, 7]

list2 = [i**2 if i >3 else i for i in list_ if i % 2 != 0]
print(list2)


dict_ = {'a': 3, 'b': 4, 'c': 5}

dict2 = {k : v + 1 if v > 3 else v for k, v in dict_.items()}
print(dict2)

вложенные словари
dict_ = {'a': {'z': 1}, 'b': {'y': 2}, 'c': {'r': 3}}

dict2 = {k : inner_v 
for k, v in dict_.items() 
for inner_v in v.values()}

print(dict2)

'============================================'






JSON - расщифровывается как JavaScript Object Notation и представляет собой
текстовый формат для хранения и обмена данными

сериализация - как упаковка
десериализация - как распаковка
json - форма, где хранится предмет, пока не доберется и не распокуется 


Для сериализации:
dump(), dumps()

dump() - принимает 2 аргумента (если не хотим сохранять данные в файлах)
сериализует питоновский объект и закидывает его в файл json

dumps() - принимает 1 аргумент 
просто сериализует питоновский объект и возвращает (объект отн-ся к str)


Пример:
import json
my_dict ={
    'name': 'Makers'
    'format': 'Bootcamp'
}
with open ('Makers.json', 'w') as my_file:
    json.dump(my_dict, my_file) #принимает 2 аргумента (1ый объект, который сериализуется, 
# 2-ой - файловый объект в который будут всписаны данные)


Создатся файл с форматом json
он будет выглядеть:
{'name': 'Makers', 'format': 'Bootcamp'}


Для десериализации (распаковки):
load(), loads()

load() - работает с json файлами

Пример:
with open ('Makers.json') as my_file:
    python_obj = json.load(my_file)
    print(python_obj)


loads() - принимает json строку и возвращает словарь

Пример:

import json
string = '{"name":"Makers", "format": "Bootcamp"}'
python_dict = json.loads(string)
print(python_dict)

выйдет {"name":"Makers", "format": "Bootcamp"}