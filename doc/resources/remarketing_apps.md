## Ремаркетинговые приложения
Источник данных для ремаркетинга. Указывают приложения в
соцсетях [Мой Мир](http://my.mail.ru/) и
[Одноклассники](http://odnoklassniki.ru/), позволяя показывать объявления
тем пользователям, которые пользовались этими приложениями или совершали
оплату.

### Создание приложения
`POST /api/v1/remarketing_apps.json`

Метод позволяет указать новое приложение в соцсетях
[Мой Мир](http://my.mail.ru/) и [Одноклассники](http://odnoklassniki.ru/)
в качестве источника данных для ремаркетинга. Метод принимает на вход
объект типа RemarketingAppForm. Он же возвращается в случае успешного
добавления приложения.

#### Пример

HTTP-запрос:

    POST /api/v1/remarketing_apps.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Content-Length: 40
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:et9e1cuhgd9aH5Gd2PJZaVyXFoQ=

    {"app_id":"259003","app_type":"mir_app"}

Curl-запрос:

    curl \
    -d '{"app_id":"259003","app_type":"mir_app"}' \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:et9e1cuhgd9aH5Gd2PJZaVyXFoQ=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_apps.json'

Пример ответа:

    {
      "app_id": "259003",
      "app_type": "mir_app",
      "id": 378,
      "name": "Шахматы"
    }


### Получение списка приложений
`GET /api/v1/remarketing_apps.json`

Метод позволяет получить список всех приложений, которые можно использовать
в качестве источника данных для ремаркетинга, в виде объектов
RemarketingAppForm.

#### Пример

HTTP-запрос:

    GET /api/v1/remarketing_apps.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:3WmDbatsLGb98ojNBJoerAE2aWs=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:3WmDbatsLGb98ojNBJoerAE2aWs=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_apps.json'

Пример ответа:

    [
      {
        "app_id": "259003",
        "app_type": "mir_app",
        "id": 378,
        "name": "Шахматы"
      }
    ]


### Удаление приложения
`DELETE /api/v1/remarketing_apps/{app_id}.json`

Метод позволяет удалить ремаркетинговое приложение. Это возможно только в
том случае, если приложение не используется ни в одной аудитории. В случае
успеха метод возвращает пустой ответ с кодом 200.

Обратите внимание на то, что в качестве идентификатора приложения метод
использует `id`, а не `app_id`.

#### Пример

HTTP-запрос:

    DELETE /api/v1/remarketing_apps/378.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:3WmDbatsLGb98ojNBJoerAE2aWs=

Curl-запрос:

    curl -X DELETE \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:3WmDbatsLGb98ojNBJoerAE2aWs=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_apps/378.json'

