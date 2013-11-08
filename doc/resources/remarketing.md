## Ремаркетинговые аудитории
Позволяют показывать объявления тем пользователям, которые
уже посещали ваш сайт ранее.

### Получение списка аудиторий
`GET /api/v1/remarketings.json`

Метод возвращает список ремаркетинговых аудиторий в виде объектов
RemarketingForm.

#### Пример

HTTP-запрос:

    GET /api/v1/remarketings.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:1YGhL7kq8af8k7tkNy2OIh5xAS8=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:1YGhL7kq8af8k7tkNy2OIh5xAS8=' \
    'https://target-sandbox.mail.ru/api/v1/remarketings.json'

Пример ответа:

    [
      {
        "disjunctions": [
          {
            "remarketing_counters": [],
            "remarketing_game_payers": [],
            "remarketing_game_players": [
              {
                "game": "259003",
                "left": 20,
                "right": 10,
                "type": "positive"
              }
            ],
            "remarketing_payers": [],
            "remarketing_players": []
          }
        ],
        "id": 1,
        "name": "Весьма тестовая аудитория"
      }
    ]


### Создание аудитории
`POST /api/v1/remarketings.json`

Метод позволяет создать ремаркетинговую аудиторию. Принимает на вход
объект типа RemarketingForm, в котором должна быть указана хотя бы одна
«дизъюнкция» с таргетингом. В случае успеха возвращает так же объект
RemarketingForm.

#### Пример

HTTP-запрос:

    POST /api/v1/remarketings.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Content-Length: 141
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:B6JnyBsDE+ZHkXt90UjW1tMNdww=

    {"name":"Особая тестовая аудитория","disjunctions":[{"remarketing_payers":[{"left":10,"right":5,"type":"positive"}]}]}

Curl-запрос:

    curl \
    -d '{"name":"Особая тестовая аудитория","disjunctions":[{"remarketing_payers":[{"left":10,"right":5,"type":"positive"}]}]}' \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:B6JnyBsDE+ZHkXt90UjW1tMNdww=' \
    'https://target-sandbox.mail.ru/api/v1/remarketings.json'

Пример ответа:

    {
      "disjunctions": [
        {
          "remarketing_counters": [],
          "remarketing_game_payers": [],
          "remarketing_game_players": [],
          "remarketing_payers": [
            {
              "left": 10,
              "right": 5,
              "type": "positive"
            }
          ],
          "remarketing_players": []
        }
      ],
      "id": 3,
      "name": "Особая тестовая аудитория"
    }


### Изменение параметров аудитории
`POST /api/v1/remarketings/{remarketing_id}.json`

Метод изменяет параметры ремаркетинговой аудитории. Параметры передаются
в виде объекта RemarketingForm. В случае успеха метод возвращает так же
объект RemarketingForm с обновлёнными параметрами.


### Удаление аудитории
`DELETE /api/v1/remarketings/{remarketing_id}.json`

Метод осуществляет удаление ремаркетинговой аудитории. Это возможно только
в том случае, если аудитория не используется ни в одной кампании, за
исключением архивных. В случае успеха возвращает пустой ответ с кодом 200.

#### Пример

HTTP-запрос:

    DELETE /api/v1/remarketings/3.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:pASFmHlVfnzZEgezKaTsfHvbqFg=

Curl-запрос:

    curl -X DELETE \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:pASFmHlVfnzZEgezKaTsfHvbqFg=' \
    'https://target-sandbox.mail.ru/api/v1/remarketings/3.json'

