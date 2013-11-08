## Ремаркетинговые группы
Источник данных для ремаркетинга. Указывают на группы
соцсети [Одноклассники](http://odnoklassniki.ru/) или на тематики групп,
позволяя показывать объявления тем пользователям, которые являются
участниками этих групп или групп определённой тематики.

### Создание группы или тематики
`POST /api/v1/remarketing_groups.json`

Метод позволяет задать группу соцсети
[Одноклассники](http://odnoklassniki.ru/) или тематику групп в качестве
источника данных для ремаркетинга. Метод принимает на вход объект типа
RemarketingGroupForm. Он же возвращается в случае успешного добавления
группы или тематики.

#### Пример

HTTP-запрос:

    POST /api/v1/remarketing_groups.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Content-Length: 43
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:79KjpYKwux4uUlWe8QjebjX5Sd4=

    {"object_id":43065395314877,"type":"group"}

Curl-запрос:

    curl \
    -d '{"object_id":43065395314877,"type":"group"}' \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:79KjpYKwux4uUlWe8QjebjX5Sd4=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_groups.json'

Пример ответа:

    {
      "id": 3,
      "name": "Mail.Ru Group",
      "object_id": 43065395314877,
      "type": "group"
    }


### Получение списка групп или тематик
`GET /api/v1/remarketing_groups.json`

Метод позволяет получить список всех групп и тематик, которые можно
использовать в качестве источника данных для ремаркетинга, в виде объектов
RemarketingGroupForm.

#### Пример

HTTP-запрос:

    GET /api/v1/remarketing_groups.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:oArysqPpqRzm37Wf/IkWIPRC8RM=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:oArysqPpqRzm37Wf/IkWIPRC8RM=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_groups.json'

Пример ответа:

    [
      {
        "id": 3,
        "name": "Mail.Ru Group",
        "object_id": 43065395314877,
        "type": "group"
      }
    ]


### Удаление группы или тематики
`DELETE /api/v1/remarketing_groups/{group_id}.json`

Метод позволяет удалить ремаркетинговую группу или тематику.
Это возможно только в том случае, если они не используется ни в одной
аудитории. В случае успеха метод возвращает пустой ответ с кодом 200.

Обратите внимание на то, что в качестве идентификатора приложения метод
использует `id`, а не `object_id`.

#### Пример

HTTP-запрос:

    DELETE /api/v1/remarketing_groups/3.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:8OCll48b+8g2t/2VxNy6d6KAO9U=

Curl-запрос:

    curl -X DELETE \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:8OCll48b+8g2t/2VxNy6d6KAO9U=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_groups/3.json'

