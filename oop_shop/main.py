from models import User
user1 = User('test@gmail.com', 'hello', 'female')
user1.register('123456789', '123456789')
user1.login('123456789')
print(user1.is_authenticated)

product1 = Product('Iphone10', 1234567, '...', 18)
comment1 = Comment(user1, product1, 'Very Good!')