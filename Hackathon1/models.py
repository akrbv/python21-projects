class Cars:
    objects = []
    _id = 0
    body_type = ['седан', 'универсал. купе', 'хэтчбек', 'минивен', 'внедорожник', 'пикап']
    def __init__(self, mark, model, year, volume, color, type_, prob, price):
        self.mark = mark
        self.model = model
        self.year = year
        self.volume = volume
        self.color = color
        self.prob = prob
        self.price = price
        if type_ in Cars.body_type:
            self.type_ = type_
        else:
            raise Exception('Выберите тип кузова из предложенных вариантов:) ')
        Cars.objects.append(self)

        Cars._id += 1
