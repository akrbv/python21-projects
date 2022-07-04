import requests

url = 'https://sputnik.kg/img/07e6/06/1e/1065723495_0:12:3072:1740_1920x0_80_0_0_1befde237ead6812bc2b64e7e2afe427.jpg.webp'
res = requests.get(url)
print(res)
name = 'photo1.jpg'

with open(name, 'wb') as file:
    file.write(res.content)
    