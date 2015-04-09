## Ремаркетинговые поисковые фразы
Списки поисковых фраз пользователей

### Удаление загруженного списка поисковых фраз
`DELETE /api/v1/remarketing_context_phrases/{context_phrases_id}.json`

Метод позволяет удалить загруженный список. Это возможно только в
том случае, если сприсок не используется ни в одной аудитории. В случае
успеха метод возвращает пустой ответ с кодом 204.

#### Пример

HTTP-запрос:

    DELETE /api/v1/remarketing_context_phrases/639.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18

Curl-запрос:

    curl -X DELETE \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_context_phrases/639.json'


### Получение списка загруженных списков поисковых фраз
`GET /api/v1/remarketing_context_phrases.json`

Метод позволяет получить список загруженных списков поисковых фраз, которые
могут быть использованы в качестве источника данных для ремаркетинга, в
виде объектов RemarketingContextPhrasesForm.

#### Пример

HTTP-запрос:

    GET /api/v1/remarketing_context_phrases.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18

Curl-запрос:

    curl \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
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

Метод позволяет загрузить список поисковых фраз в качестве источника данных
для ремаркетинга. В случае успешной загрузки возвращается объект типа
RemarketingContextPhrasesForm.

В отличие от других POST-запросов к API, имеющих тип `application/json`,
запрос на загрузку файла с фразами должен иметь тип `multipart/form-data`.
Сам файл для загрузки нужно передавать как часть multipart-запроса
с именем `file`. Название списка `name` нужно передавать также в
multipart-виде.

#### Пример

Для загрузки в примере используется файл test.txt с содержимым: test,hello

HTTP-запрос:

    POST /api/v1/remarketing_context_phrases.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18
    Content-Length: 294
    Content-Type: multipart/form-data; boundary=------------------------6f6445c8f1dc5d8e


Curl-запрос:

    curl -F file=@test.txt  -F name=test \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_context_phrases.json'

Пример ответа:

    {
      "id": 10,
      "name": "test",
    }

