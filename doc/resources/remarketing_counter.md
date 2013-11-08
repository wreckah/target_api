## Ремаркетинговые счётчики
Источник данных для ремаркетинга. Указывает счётчики
[top.mail.ru](http://top.mail.ru/), на основании данных от которых
происходит определение того, посещал ли пользователь ваш сайт ранее.

### Получение списка счётчиков
`GET /api/v1/remarketing_counters.json`

Метод позволяет получить список счётчиков, которые могут быть использованы
в качестве источника данных для ремаркетинга, в виде объектов
RemarketingCounterForm.

#### Пример

HTTP-запрос:

    GET /api/v1/remarketing_counters.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:jQMzjyCaLVC6vWotOlngHrzbv/M=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:jQMzjyCaLVC6vWotOlngHrzbv/M=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_counters.json'

Пример ответа:

    [
      {
        "counter_id": 2381587,
        "goals": [
          {
            "goal_id": "uss:/our_base/",
            "name": "Our base is under attack",
            "status": "active"
          }
        ],
        "id": 639,
        "name": "Strange Encounter",
        "status": "active",
        "system_status": "active"
      }
    ]


### Создание счётчика
`POST /api/v1/remarketing_counters.json`

Метод позволяет указать новый счётчик [top.mail.ru](http://top.mail.ru/) в
качестве источника данных для ремаркетинга. Метод принимает на вход объект
типа RemarketingCounterForm. Он же возвращается в случае успешного
добавления счётчика.

Добавить счётчик может только владелец счётчика (email-адрес владельца
счётчика совпадает с email-адресом вашего аккаунта) либо пользователь,
который имеет доступ к этому счётчику (владелец может дать доступ к
счётчику, указав email-адрес другого пользователя). В противном
случае метод вернёт ответ с кодом 400 и соответствующим сообщением. Если
вы уверены, что хотите использовать этот счётчик для ремаркетинга, можно
послать повторный запрос с указанием `system_status=active`. Тогда
будет создан неактивный счётчик, а владельцу будет отправлен запрос на
подтверждение. В случае получения разрешения владельца счётчик будет
активирован автоматически.

Если счётчика с указанным в запросе `counter_id` не существует, метод
вернёт ответ с кодом 404.

#### Пример

HTTP-запрос:

    POST /api/v1/remarketing_counters.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Content-Length: 23
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:ULODrcrSJItYUP+rERziZW3ONkg=

    {"counter_id": 2381587}

Curl-запрос:

    curl \
    -d '{"counter_id": 2381587}' \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:ULODrcrSJItYUP+rERziZW3ONkg=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_counters.json'

Пример ответа:

    {
      "counter_id": 2381587,
      "goals": [
        {
          "goal_id": "uss:/our_base/",
          "name": "Our base is under attack",
          "status": "active"
        }
      ],
      "id": 639,
      "name": "Strange Encounter",
      "status": "active",
      "system_status": "active"
    }


### Получение информации о счётчике
`GET /api/v1/remarketing_counters/{counter_id}.json`

Метод позволяет получить информацию о ремаркетинговом счётчике в виде
объекта RemarketingCounterForm.

Обратите внимание на то, что в качестве идентификатора счётчика метод
использует `id`, а не `counter_id`.

#### Пример

HTTP-запрос:

    GET /api/v1/remarketing_counters/639.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:o5cgpk8aDEGuFbrNF1WUX0UIXHQ=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:o5cgpk8aDEGuFbrNF1WUX0UIXHQ=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_counters/639.json'

Пример ответа:

    {
      "counter_id": 2381587,
      "goals": [
        {
          "goal_id": "uss:/our_base/",
          "name": "Our base is under attack",
          "status": "active"
        }
      ],
      "id": 639,
      "name": "Strange Encounter",
      "status": "active",
      "system_status": "active"
    }


### Обновление параметров счётчика
`POST /api/v1/remarketing_counters/{counter_id}.json`

Метод позволяет изменить значение параметров ремаркетингового счётчика.
На вход принимается объект типа RemarketingCounterForm, он же возвращается
в случае успешного завершения.

Обратите внимание на то, что в качестве идентификатора счётчика метод
использует `id`, а не `counter_id`.

#### Пример

HTTP-запрос:

    POST /api/v1/remarketing_counters/639.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Content-Length: 18
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:92s8jYaiPL4UDmXGrx1p13VyKos=

    {"name": "noname"}

Curl-запрос:

    curl \
    -d '{"name": "noname"}' \
    -H 'Authorization: AuthHMAC Bv2BaJv95g68G39:92s8jYaiPL4UDmXGrx1p13VyKos=' \
    'https://target-sandbox.mail.ru/api/v1/remarketing_counters/639.json'

Пример ответа:

    {
      "counter_id": 2381587,
      "goals": [
        {
          "goal_id": "uss:/our_base/",
          "name": "Our base is under attack",
          "status": "active"
        }
      ],
      "id": 639,
      "name": "noname",
      "status": "active",
      "system_status": "active"
    }


### Удаление счётчика
`DELETE /api/v1/remarketing_counters/{counter_id}.json`

Метод позволяет удалить ремаркетинговый счётчик. Это возможно только в
том случае, если счётчик не используется ни в одной аудитории. В случае
успеха метод возвращает пустой ответ с кодом 200.

Обратите внимание на то, что в качестве идентификатора счётчика метод
использует `id`, а не `counter_id`.

