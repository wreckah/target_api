## Ремаркетинговые поисковые фразы
Списки поисковых фраз пользователей

### Удаление загруженного списка поисковых фраз
`DELETE /api/v1/remarketing_context_phrases/{context_phrases_id}.json`

Метод позволяет удалить загруженный список. Это возможно только в
том случае, если сприсок не используется ни в одной аудитории. В случае
успеха метод возвращает пустой ответ с кодом 200.

#### Пример

HTTP-запрос:

    DELETE /api/v1/remarketing_context_phrases/639.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:FF1jn812BNwhUP5EF6+J68lbtvE=

Curl-запрос:

    curl -X DELETE \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:FF1jn812BNwhUP5EF6+J68lbtvE=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_context_phrases/639.json'


### Получение списка загруженных списков поисковых фраз
`GET /api/v1/remarketing_context_phrases.json`

Метод позволяет получить список загруженных списков поисковых фраз, которые могут быть использованы
в качестве источника данных для ремаркетинга, в виде объектов
RemarketingContextPhrasesForm.

#### Пример

HTTP-запрос:

    GET /api/v1/remarketing_context_phrases.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:S/EG1ZDUcql3G3n4KVcYX0YI4s8=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:S/EG1ZDUcql3G3n4KVcYX0YI4s8=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_context_phrases.json'

Пример ответа:

    [
      {
        "id": 1,
        "name": "context"
      },
      {
        "id": 6,
        "name": "phrases"
      },
      {
        "id": 7,
        "name": "test"
      }
    ]


### Загрузка списка поисковых фраз
`POST /api/v1/remarketing_context_phrases.json`

Метод позволяет загрузить список поисковых фраз в качестве источника данных для ремаркетинга.
В случае успешной загрузки возвращается объект типа RemarketingContextPhrasesForm

Алгоритм подписи запроса на загрузку файла немного отличается от
стандартного. В запросе необходимо передать HTTP-заголовок `X-Trg-Chksum`,
который содержит хэш-сумму от загружаемого файла, полученную по
алгоритму `MD5`. Кроме того, при создании подписи вместо тела POST-запроса
нужно использовать эту же хэш-сумму.

В отличие от других POST-запросов к API, имеющих тип `application/json`,
запрос на загрузку изображения должен иметь тип `multipart/form-data`.
Сам файл для загрузки нужно передавать как часть multipart-запроса
с именем `file`. Название списка `name` нужно передавать также в
multipart-виде.

#### Пример

Для загрузки в примере используется файл test.txt с содержимым: test,hello

HTTP-запрос:

    POST /api/v1/remarketing_context_phrases.json HTTP/1.1
    Host: target-sandbox.mail.ru
    X-Trg-Chksum: 416f1b5e2e694ed5716666c694a2bdf4
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:mdU/UuTRjdXecT41c4g6zr5AiH0=
    Content-Length: 294
    Content-Type: multipart/form-data; boundary=------------------------6f6445c8f1dc5d8e


Curl-запрос:

    curl -F file=@test.txt  -F name=test \
    -H 'X-Trg-Chksum: 416f1b5e2e694ed5716666c694a2bdf4' \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:mdU/UuTRjdXecT41c4g6zr5AiH0=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_context_phrases.json'

Пример ответа:

    {
      "id": 10,
      "name": "test",
    }

