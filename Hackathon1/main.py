from utils import urlpatterns
from pprint import pprint

while True:
    try:
        url, arg = input("Добро пожаловать в магазин 'CARS'\nВы можете выбрать одну из опций:\n(listing/, create/, retrieve/, update/ , delete/): ") .split("/")
    except ValueError:
        print("Вы ввели некоррекный запрос :) Попробуйте ещё раз! ")
        continue

    found = False
    for uri, view in urlpatterns:
        if uri.split("/")[0] == url:
            found = True

            try:
                if arg:
                    pprint(view(arg))
                else:
                    pprint(view())
            except Exception as e:
                print(e)
