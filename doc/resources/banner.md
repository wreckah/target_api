## Рекламные объявления


### Получение информации об объявлении
`GET /api/v1/banners/{banner_id}.json`

Метод возвращает полную информацию об объявлении в виде объекта
BannerStatForm. Возможно передать несколько значений `{banner_id}`,
разделённых точкой с запятой (`;`). В таком случае метод вернёт список
объектов BannerStatForm.

Список полей объявления, перечисленных через запятую, задаётся параметром
`fields`. Возможные значения соответствуют названиям полей объекта
BannerStatForm.

#### Пример

HTTP-запрос:

    GET /api/v1/banners/687419.json HTTP/1.1
    Host: target-sandbox.my.com
    Accept-Encoding: gzip, deflate, compress
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18

Curl-запрос:

    curl \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
    'https://target-sandbox.my.com/api/v1/banners/687419.json'

Пример ответа:

    {
      "banner_fields": [
        "title",
        "text",
        "url",
        "image"
      ],
      "banner_moderation": {
        "moderation_comment": "",
        "moderation_reason": ""
      },
      "campaign": {
        "id": 334648,
        "url": "/api/v1/campaigns/334648.json"
      },
      "company_name": "",
      "created": "2013-06-27 13:50:09",
      "edit_url": "/ads/banners/687419/edit/",
      "id": 687419,
      "image": {
        "height": 45,
        "id": 24513,
        "is_animated": false,
        "preview_url": "https://rb.mail.ru/img/BA/573CCB.jpg",
        "size": 1616,
        "type": "static",
        "url": "http://r.mail.ru/img/BA/573CCB.jpg",
        "width": 60
      },
      "json_url": "/api/v1/banners/687419.json",
      "moderation_reason_display": "",
      "moderation_status": "new",
      "preview_image_url": "https://rb.mail.ru/img/BA/573CCB.jpg",
      "stats": {
        "amount": "0.00",
        "clicks": 0,
        "shows": 0
      },
      "stats_today": {
        "amount": "0.00",
        "clicks": 0,
        "shows": 0
      },
      "stats_yesterday": {
        "amount": "0.00",
        "clicks": 0,
        "shows": 0
      },
      "status": "active",
      "system_status": "active",
      "telephone": "",
      "text": "Кот кататься не привык, опрокинул грузовик.",
      "title": "Accident",
      "updated": "2013-06-28 13:07:09",
      "url": "http://wikipedia.org/",
      "user": {
        "id": 1030027
      }
    }


### Изменение параметров объявления
`POST /api/v1/banners/{banner_id}.json`

Метод изменяет параметры объявления, переданные в запросе в виде объекта
BannerForm. В случае успешного изменения в ответе возвращается объект
BannerForm с изменёнными параметрами.

Возможно передать несколько значений `{banner_id}`, разделённых точкой
с запятой (`;`). В таком случае метод обновит список объектов BannerForm.

Список полей баннера, которые вернутся в ответе, перечисленных через запятую,
задаётся параметром `fields`. Возможные значения соответствуют названиям
полей объекта BannerForm.

#### Пример

HTTP-запрос:

    POST /api/v1/banners/687419.json HTTP/1.1
    Host: target-sandbox.my.com
    Content-Type: application/json
    Content-Length: 37
    Accept-Encoding: gzip, deflate, compress
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18

    {"title": "\u0442\u0435\u0441\u0442"}

Curl-запрос:

    curl \
    -d '{"title": "\u0442\u0435\u0441\u0442"}' \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
    'https://target-sandbox.my.com/api/v1/banners/687419.json'

Пример ответа:

    {
      "moderation_reason_display": "",
      "moderation_status": "new",
      "status": "active",
      "system_status": "active",
      "title": "тест"
    }


### Получение списка всех объявлений кампании
`GET /api/v1/campaigns/{campaign_id}/banners.json`

Метод позволяет получить список всех объявлений (объектов типа BannerForm),
относящихся к указанной рекламной кампании, с возможностью
фильтрации по статусу.

Значение для фильтрации по статусу объявления задаётся GET-параметром
`status`. Возможные значения: `active`, `blocked`, `deleted`. Символ `-`
перед значением статуса инвертирует фильтр.

#### Пример

HTTP-запрос:

    GET /api/v1/campaigns/334648/banners.json HTTP/1.1
    Host: target-sandbox.my.com
    Accept-Encoding: gzip, deflate, compress
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18

Curl-запрос:

    curl \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
    'https://target-sandbox.my.com/api/v1/campaigns/334648/banners.json'

Пример ответа:

    [
      {
        "banner_fields": [
          "title",
          "text",
          "url",
          "image"
        ],
        "banner_moderation": {
          "moderation_comment": "",
          "moderation_reason": ""
        },
        "campaign": {
          "id": 334648,
          "url": "/api/v1/campaigns/334648.json"
        },
        "company_name": "",
        "created": "2013-06-26 22:57:20",
        "edit_url": "/ads/banners/687418/edit/",
        "id": 687418,
        "image": {
          "height": 45,
          "id": 24512,
          "is_animated": false,
          "preview_url": "https://rb.mail.ru/img/36/6C4A7E.jpg",
          "size": 1607,
          "type": "static",
          "url": "http://r.mail.ru/img/36/6C4A7E.jpg",
        },
        "json_url": "/api/v1/banners/687418.json",
        "moderation_reason_display": "",
        "moderation_status": "allowed",
        "preview_image_url": "https://rb.mail.ru/img/36/6C4A7E.jpg",
        "status": "active",
        "system_status": "active",
        "telephone": "",
        "text": "Testov",
        "title": "Test",
        "updated": "2013-06-27 13:50:30",
        "url": "http://mail.ru/",
        "user": {
          "id": 1030027
        }
      },
      {
        "banner_fields": [
          "title",
          "text",
          "url",
          "image"
        ],
        "banner_moderation": {
          "moderation_comment": "",
          "moderation_reason": ""
        },
        "campaign": {
          "id": 334648,
          "url": "/api/v1/campaigns/334648.json"
        },
        "company_name": "",
        "created": "2013-06-27 13:50:09",
        "edit_url": "/ads/banners/687419/edit/",
        "id": 687419,
        "image": {
          "height": 45,
          "id": 24513,
          "is_animated": false,
          "preview_url": "https://rb.mail.ru/img/BA/573CCB.jpg",
          "size": 1616,
          "type": "static",
          "url": "http://r.mail.ru/img/BA/573CCB.jpg",
          "width": 60
        },
        "json_url": "/api/v1/banners/687419.json",
        "moderation_reason_display": "",
        "moderation_status": "new",
        "preview_image_url": "https://rb.mail.ru/img/BA/573CCB.jpg",
        "status": "active",
        "system_status": "active",
        "telephone": "",
        "text": "Кот кататься не привык, опрокинул грузовик.",
        "title": "тест",
        "updated": "2013-06-28 15:21:29",
        "url": "http://wikipedia.org/",
        "user": {
          "id": 1030027
        }
      }
    ]


### Создание объявления
`POST /api/v1/campaigns/{campaign_id}/banners.json`

Метод позволяет создать рекламное объявление с параметрами, переданными в
виде объекта BannerForm. В случае успеха в ответе возвращается также объект
типа BannerForm со всеми параметрами созданного объявления.

Кроме того, метод может принимать на вход список объектов BannerForm.
Это позволяет создать несколько объявлений в кампании одним запросом.

#### Пример

HTTP-запрос:

    POST /api/v1/campaigns/334648/banners.json HTTP/1.1
    Host: target-sandbox.my.com
    Content-Type: application/json
    Content-Length: 671
    Accept-Encoding: gzip, deflate, compress
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18

    {"text":"тестовое объявление","title":"тест","image":{"id":24512},"url":"http://test.ru/"}

Curl-запрос:

    curl \
    -d '{"text":"тестовое объявление","title":"тест","image":{"id":24512},"url":"http://test.ru/"}' \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
    'https://target-sandbox.my.com/api/v1/campaigns/334648/banners.json'

Пример ответа:

    {
      "banner_fields": [
        "title",
        "text",
        "url",
        "image"
      ],
      "banner_moderation": {
        "moderation_comment": "",
        "moderation_reason": ""
      },
      "campaign": {
        "id": 334648,
        "url": "/api/v1/campaigns/334648.json"
      },
      "company_name": "",
      "created": "2013-06-29 17:58:03",
      "edit_url": "/ads/banners/687424/edit/",
      "id": 687424,
      "image": {
        "height": 45,
        "id": 24512,
        "is_animated": false,
        "preview_url": "https://rb.mail.ru/img/36/6C4A7E.jpg",
        "size": 1607,
        "type": "static",
        "url": "http://r.mail.ru/img/36/6C4A7E.jpg",
        "width": 60
      },
      "json_url": "/api/v1/banners/687424.json",
      "moderation_reason_display": "",
      "moderation_status": "new",
      "preview_image_url": "https://rb.mail.ru/img/36/6C4A7E.jpg",
      "status": "active",
      "system_status": "active",
      "telephone": "",
      "text": "тестовое объявление",
      "title": "тест",
      "updated": "2013-06-29 17:58:03",
      "url": "http://test.ru/",
      "user": {
        "id": 1030027
      }
    }


### Получение списка всех рекламных объявлений пользователя
`GET /api/v1/banners.json`

Метод позволяет получить список всех объявлений (объектов типа
BannerStatForm), принадлежащих текущему пользователю, с возможностью
фильтрации по статусу как самих объявлений, так и кампаний, к которым они
относятся.

Значение для фильтрации по статусу объявления задаётся GET-параметром
`status`. Возможные значения: `active`, `blocked`, `deleted`. Символ `-`
перед значением статуса инвертирует фильтр.

Значение для фильтрации по статусу кампании, которой принадлежит
объявление, задаётся параметром `campaign__status`. Параметр имеет те же
допустимые значения и принимает символ `-` в начале.

#### Пример

HTTP-запрос:

    GET /api/v1/banners.json HTTP/1.1
    Host: target-sandbox.my.com
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18

Curl-запрос:

    curl \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
    'https://target-sandbox.my.com/api/v1/banners.json'

Пример ответа:

    [
      {
        "banner_fields": [
          "title",
          "text",
          "url",
          "image"
        ],
        "banner_moderation": {
          "moderation_comment": "Объявление не содержит осмысленного текста.",
          "moderation_reason": "CUSTOM"
        },
        "campaign": {
          "id": 268888,
          "url": "/api/v1/campaigns/268888.json"
        },
        "company_name": "",
        "created": "2011-09-08 17:23:43",
        "edit_url": "/ads/banners/529397/edit/",
        "id": 529397,
        "image": {
          "height": 31,
          "id": 6132,
          "is_animated": false,
          "preview_url": "https://rb.mail.ru/img/37/1FC5FA.png",
          "size": 3975,
          "type": "static",
          "url": "http://r.mail.ru/img/37/1FC5FA.png",
          "width": 60
        },
        "json_url": "/api/v1/banners/529397.json",
        "moderation_reason_display": "Объявление не содержит осмысленного текста.",
        "moderation_status": "banned",
        "preview_image_url": "https://rb.mail.ru/img/37/1FC5FA.png",
        "stats": {
          "amount": "0.00",
          "clicks": 0,
          "shows": 0
        },
        "stats_today": {
          "amount": "0.00",
          "clicks": 0,
          "shows": 0
        },
        "stats_yesterday": {
          "amount": "0.00",
          "clicks": 0,
          "shows": 0
        },
        "status": "deleted",
        "system_status": "active",
        "telephone": "",
        "text": "Test Kirillov. Test Kirillov",
        "title": "Test Kirillov",
        "updated": "2013-06-11 19:00:09",
        "url": "http://ya.ru/",
        "user": {
          "id": 1007846
        }
      }
    ]

