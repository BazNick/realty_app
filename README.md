# realty_app

- Для сборки приложения: docker-compose build
- Для работы приложения: docker-compose up

Для проверки приложения (пример с Postman): 

1) Кинуть POST запрос на http://localhost:8000/api/token 

2) В теле запроса (Body) выбрать *x-www-form-urlencoded* и написать 2 *key-value* **username=nick** **password=12345** (Это примеры, можно завести своих пользователей в админке использовав те же username и пароль) и отправить (Send).
В ответе придут 2 токена: access и refresh токены.

3) Для проверки работоспособности можно кинуть два GET запроса (в том же Postman):

4) Получить среднюю цену продажи в среднем по городу в заданном диапазоне дат: http://localhost:8000/api/average-price?date_start=2023-10-01&date_end=2023-12-31
предварительно передав в *headers* заголовок: **key=Authorization** **value=Bearer вернувшийся_access_токен**

5) Получить предложения в диапазоне цен (price_start, price_end) по списку городов: http://localhost:8000/api/offers?price_start=0&price_end=10000&cities=Moscow,New-York
предварительно передав в *headers* заголовок: **key=Authorization** **value=Bearer вернувшийся_access_токен**






