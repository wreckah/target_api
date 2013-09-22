## Тематики групп в Одноклассниках
Тематики групп в соцсети
[Одноклассники](http://odnoklassniki.ru/)

### Получение списка тематик групп
`GET /api/v1/odkl_group_scopes.json`

Метод позволяет получить список тематик групп соцсети
[Одноклассники](http://odnoklassniki.ru/) в виде объектов
OdklGroupScopeForm для дальнейшего использования их в качестве источника
данных для ремаркетинга.

#### Пример

HTTP-запрос:

    GET /api/v1/odkl_group_scopes.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:obZYc8pJH+Y1a9SFOHUptSHvaxE=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:obZYc8pJH+Y1a9SFOHUptSHvaxE=' \
    'https://target-sandbox.mail.ru/api/v1/odkl_group_scopes.json'

Пример ответа:

    [
      {
        "id": 9,
        "name": "Авто и мото"
      },
      ...
      {
        "id": 3,
        "name": "Игры"
      },
      ...
      {
        "id": 0,
        "name": "Музыка"
      },
      ...
    ]

