# Задание 3: Отправка данных
# Используйте API, которое принимает POST-запросы для создания новых данных
# (например, https://jsonplaceholder.typicode.com/posts).
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
# Отправьте POST-запрос с этими данными.

import pprint
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title' : 'foo',
    'body' : 'bar',
    'userId' : 1
}
response = requests.post(url, data=data)

print(response.status_code)
print(f"ответ: {response.json()}")

