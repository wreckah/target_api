## Группы в Одноклассниках
Группы в соцсети
[Одноклассники](http://odnoklassniki.ru/)

### Получение списка групп
`GET /api/v1/odkl_groups.json`

Метод позволяет получить список групп соцсети
[Одноклассники](http://odnoklassniki.ru/) в виде объектов
OdklGroupsForm для дальнейшего использования их в качестве источника
данных для ремаркетинга.

Список формируется в результате поиска групп по вхождению поисковой фразы
в название группы. Поисковая фраза задаётся GET-параметром `q`.
Ограничить количество результатов поиска можно GET-параметром `limit`.
Значение `limit` «по умолчанию» — 10. Максимальное значение — 100.

#### Пример

HTTP-запрос:

    GET /api/v1/odkl_groups.json?q=mail.ru HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:A2m1j3ogy9fT0Ww+qb8/X2KhwgU=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:A2m1j3ogy9fT0Ww+qb8/X2KhwgU=' \
    'https://target-sandbox.mail.ru/api/v1/odkl_groups.json?q=mail.ru'

Пример ответа:

    [
      {
        "id": 53669865652234,
        "title": "agent@mail.ru"
      },
      {
        "id": 53708832309250,
        "title": "Mail.Ru Games"
      },
      {
        "id": 43065395314877,
        "title": "Mail.Ru Group"
      },
      ...
    ]

*Generated automatically at 2013-09-23 00:26:16.062876*