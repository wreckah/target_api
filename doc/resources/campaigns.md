## Рекламные кампании


### Получение списка кампаний
`GET /api/v1/campaigns.json`

Метод позволяет получить список рекламных кампаний (объектов типа
CampaignStatForm) с возможностью фильтрации по статусу и указания полей
кампании, которые будут присутствовать в ответе.

Статус для фильтрации задаётся GET-параметром `status`. Возможные значения:
`active`, `blocked`, `deleted`. Символ `-` перед значением статуса
инвертирует фильтр.

Список полей кампании, перечисленных через запятую, задаётся параметром
`fields`. Возможные значения соответствуют названиям полей объекта
CampaignStatForm.

Чтобы получить список кампаний с баннерам задается GET-параметр
`with_banners=1`.

#### Пример

HTTP-запрос:

    GET /api/v1/campaigns.json?status=active&fields=id%2Cname%2Ccreated%2Cbudget_limit HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:/Sgea5u8hApgEHQ/hPwQFF8mgXM=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:/Sgea5u8hApgEHQ/hPwQFF8mgXM=' \
    'https://target-sandbox.mail.ru/api/v1/campaigns.json?status=active&fields=id,name,created,budget_limit'

Пример ответа:

    [
      {
        "id": 334644,
        "name": "Test campaign",
        "budget_limit": "",
        "created": "2013-06-17 12:47:29",
      }
    ]


### Создание кампании
`POST /api/v1/campaigns.json`

Метод создаёт рекламную кампанию, принимая на вход её параметры в виде
объекта CampaignForm. В случае успешного создания также возвращает объект
CampaignForm. Одним из обязательных параметров является идентификатор
пакета, в рамках которого создаётся кампания.

#### Пример

HTTP-запрос:

    POST /api/v1/campaigns.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Content-Length: 136
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:/Sgea5u8hApgEHQ/hPwQFF8mgXM=

    {"name": "Test campaign", "package": {"id": 18}, "targetings": {"regions": [188], "sex": "MF", "age": [20, 21], "pads": [{"id": 5206}]}}

Curl-запрос:

    curl \
    -d '{"name": "Test campaign", "package": {"id": 18}, "targetings": {"regions": [188], "sex": "MF", "age": [20, 21], "pads": [{"id": 5206}]}}' \
    -H 'Authorization: AuthHMAC Bv2BaJv95g68G39:j8bVRc445dgH6S9MO9+/y6zUeQE=' \
    'https://target-sandbox.mail.ru/api/v1/campaigns.json'

Пример ответа:

    {
      "autobidding_mode": "fixed",
      "avg_api_ctr": 0.0,
      "avg_ctr": 0.0,
      "banners_count": 0,
      "banners_ctr_api_list": [],
      "banners_url": "/api/v1/campaigns/334646/banners.json",
      "budget_limit": "",
      "budget_limit_day": "",
      "created": "2013-06-25 21:31:05",
      "date_end": "",
      "date_start": "",
      "edit_url": "/ads/campaigns/334646/edit/",
      "group_members": "all",
      "id": 334646,
      "max_api_ctr": 0.0,
      "max_ctr": 0.0,
      "min_api_ctr": 0.0,
      "min_ctr": 0.0,
      "mixing": "recommended",
      "name": "Test campaign",
      "package": {
        "banner_format": {
          "description": "\u0422\u0438\u0437\u0435\u0440 (\u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 60\u044575 \u0442\u0435\u043a\u0441\u0442)",
          "fields": [
            "title",
            "text",
            "url",
            "image"
          ],
          "fields_": {
            "image": {
              "height": 75,
              "type": [
                "static",
                "rollovered"
              ],
              "width": 60
            },
            "text": {
              "max_length": 90,
              "required": true,
              "visible": true
            },
            "title": {
              "max_length": 25,
              "required": true,
              "visible": true
            },
            "url": {
              "required": true,
              "visible": true
            }
          },
          "id": 1,
          "image": {
            "height": 75,
            "type": [
              "static",
              "rollovered"
            ],
            "width": 60
          },
          "name": "teaser"
        },
        "base_cpm_limit": "2.5",
        "base_price_per_click": "0",
        "base_price_per_show": "0.0015",
        "description": "\u041c\u043e\u0439 \u041c\u0438\u0440: \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u0441\u0441\u044b\u043b\u043a\u0438, \u043f\u043e\u043a\u0430\u0437\u044b",
        "eye_url": "http://my.mail.ru/community/targetmailru",
        "eye_urls": [
          {
            "description": "\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043d\u0430 \u041c\u043e\u0435\u043c \u041c\u0438\u0440\u0435",
            "url": "http://my.mail.ru/community/targetmailru"
          }
        ],
        "features": {
          "extended_age_targetings": true,
          "product_type": "game",
          "promo_id": [],
          "required_targetings": [
            "sex",
            "age",
            "day_hours",
            "week_days",
            "pads"
          ],
          "settings": {
            "mixing": {}
          },
          "targetings": [
            "-regions"
          ],
          "targetings_": [
            "age",
            "grouped_regions_names",
            "pads",
            "birthday",
            "sex",
            "regions_names",
            "fulltime"
          ],
          "url_type": "mir_redirect"
        },
        "highest_price_per_unit": "0.0015",
        "id": 18,
        "is_external": false,
        "max_price_per_unit": "60",
        "name": "mir_int",
        "price_per_click": "0",
        "price_per_show": "0.0015",
        "slider_positions": {
          "blue_zone": 4.3,
          "max_price": 60.0,
          "min_price": 1.5,
          "overcompetitive_price": 4.3,
          "recommended_price": 2.9,
          "red_zone": 1.5
        },
        "status": "active",
        "system_status": "active",
        "targetings": {
          "pads": [
            {
              "description": "\u0414\u0440\u0443\u0433\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u044b",
              "eye_url": {
                "description": "\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043d\u0430 \u041c\u043e\u0435\u043c \u041c\u0438\u0440\u0435",
                "id": 2,
                "url": "http://my.mail.ru/community/targetmailru"
              },
              "id": 3002,
              "name": "mail_other_abstract"
            },
            {
              "description": "\u041f\u0440\u043e\u0444\u0438\u043b\u0438",
              "eye_url": {
                "description": "\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043d\u0430 \u041c\u043e\u0435\u043c \u041c\u0438\u0440\u0435",
                "id": 2,
                "url": "http://my.mail.ru/community/targetmailru"
              },
              "id": 3003,
              "name": "mail_mir_abstract"
            },
            {
              "description": "\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f",
              "eye_url": {
                "description": "\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043d\u0430 \u041c\u043e\u0435\u043c \u041c\u0438\u0440\u0435",
                "id": 2,
                "url": "http://my.mail.ru/community/targetmailru"
              },
              "id": 4080,
              "name": "mail_mir_apps"
            }
          ]
        }
      },
      "price_per_click": "0",
      "price_per_show": "0.0015",
      "slider_positions": {
        "blue_zone": 4.3,
        "max_price": 60.0,
        "min_price": 1.5,
        "overcompetitive_price": 4.3,
        "recommended_price": 2.9,
        "red_zone": 1.5
      },
      "stats": {
        "amount": "0.00",
        "clicks": 0,
        "shows": 0
      },
      "status": "active",
      "system_status": "active",
      "targetings": {
        "age": [
          20,
          21
        ],
        "birthday": {
          "days_after": null,
          "days_before": null
        },
        "current_game": false,
        "day_hours": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "education": [],
        "fulltime": {
          "flags": [
            "cross_timezone",
            "use_holidays_moving"
          ],
          "fri": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "mon": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "sat": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "sun": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "thu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "tue": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "wed": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        },
        "grouped_regions_names": [],
        "language": {
          "english": [],
          "french": [],
          "german": []
        },
        "mobile_operation_systems": [],
        "mobile_region": [],
        "mobile_vendors": [],
        "interests": [],
        "pads": [
          {
            "description": "\u0414\u0440\u0443\u0433\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u044b",
            "eye_url": {
              "description": "\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043d\u0430 \u041c\u043e\u0435\u043c \u041c\u0438\u0440\u0435",
              "id": 2,
              "url": "http://my.mail.ru/community/targetmailru"
          },
            "id": 3002,
            "name": "mail_other_abstract"
          }
        ],
        "paid": "all",
        "profession": [],
        "regions": [],
        "regions_names": [],
        "remarketing": [],
        "salary": [],
        "sex": "FMU",
        "thematics": [],
        "tree": [],
        "user_geo": null,
        "week_days": [
          "mon",
          "tue",
          "wed",
          "thu",
          "fri",
          "sat",
          "sun"
        ]
      },
      "updated": "2013-06-25 21:31:05",
      "url": "/api/v1/campaigns/334646.json"
  }


### Получение информации о кампании
`GET /api/v1/campaigns/{campaign_id}.json`

Метод возвращает полную информацию о рекламной кампании в виде объекта
CampaignStatForm. Возможно передать несколько значений `{campaign_id}`,
разделённых точкой с запятой (`;`).

#### Пример

HTTP-запрос:

    GET /api/v1/campaigns/334648.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:OTPf3hv2pdkVhVrk6TlrmqJcISQ=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:OTPf3hv2pdkVhVrk6TlrmqJcISQ=' \
    'https://target-sandbox.mail.ru/api/v1/campaigns/334648.json'

Пример ответа:

    {
      "autobidding_mode": "second_price_mean",
      "banners_count": 2,
      "banners_url": "/api/v1/campaigns/334648/banners.json",
      "budget_limit": "",
      "budget_limit_day": "",
      "created": "2013-06-26 22:57:19",
      "date_end": "",
      "date_start": "",
      "edit_url": "/ads/campaigns/334648/edit/",
      "group_members": "all",
      "id": 334648,
      "last_updated": "2013-06-28 13:07:09",
      "mixing": "recommended",
      "name": "Новая кампания 2013-06-26",
      "package": {
        "banner_format": {
          "description": "Тизер (изображение 60х75 текст)",
          "fields": [
            "title",
            "text",
            "url",
            "image"
          ],
          "fields_": {
            "image": {
              "height": 75,
              "type": [
                "static",
                "rollovered"
              ],
              "width": 60
            },
            "text": {
              "max_length": 90,
              "required": true,
              "visible": true
            },
            "title": {
              "max_length": 25,
              "required": true,
              "visible": true
            },
            "url": {
              "required": true,
              "visible": true
            }
          },
          "id": 1,
          "image": {
            "height": 75,
            "type": [
              "static",
              "rollovered"
            ],
            "width": 60
          },
          "name": "teaser"
        },
        "base_cpm_limit": "1.5",
        "base_price_per_click": "4",
        "base_price_per_show": "0",
        "description": "Внешние ссылки, клики",
        "eye_url": "http://www.odnoklassniki.ru/target",
        "eye_urls": [
          {
            "description": "Посмотреть на Одноклассниках",
            "url": "http://www.odnoklassniki.ru/target"
          }
        ],
        "features": {
          "has_auction_strategy": true,
          "product_type": "external",
          "promo_id": [],
          "required_targetings": [
            "sex",
            "age",
            "regions",
            "day_hours",
            "week_days",
            "pads"
          ],
          "settings": {
            "autobidding_mode": {},
            "mixing": {}
          },
          "targetings_": [
            "user_geo",
            "age",
            "grouped_regions_names",
            "sex",
            "regions",
            "pads",
            "birthday",
            "fulltime",
            "remarketing",
            "regions_names",
            "thematics"
          ],
          "url_type": "external_new"
        },
        "highest_price_per_unit": "5.5",
        "id": 65,
        "is_external": true,
        "max_price_per_unit": "60",
        "name": "multiple_external_ppc",
        "price_per_click": "1.5",
        "price_per_show": "0",
        "slider_positions": {
          "blue_zone": 5.5,
          "max_price": 60.0,
          "min_price": 1.5,
          "overcompetitive_price": 5.5,
          "recommended_price": 4.0,
          "red_zone": 1.5
        },
        "status": "active",
        "system_status": "active",
        "targetings": {
          "pads": [
            {
              "description": "Социальные сети и сервисы (Одноклассники.Ру, МойМир@Mail.Ru, Почта@Mail.ru и др.)",
              "eye_url": {
                "description": "Посмотреть на Одноклассниках",
                "id": 1,
                "url": "http://www.odnoklassniki.ru/target"
              },
              "id": 5206,
              "name": "social_abstract"
            }
          ]
        }
      },
      "price_per_click": "5.5",
      "price_per_show": "0",
      "slider_positions": {
        "blue_zone": 5.5,
        "max_price": 60.0,
        "min_price": 1.5,
        "overcompetitive_price": 5.5,
        "recommended_price": 4.0,
        "red_zone": 1.5
      },
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
      "targetings": {
        "age": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        "birthday": {
          "days_after": null,
          "days_before": null
        },
        "current_game": null,
        "day_hours": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
        "education": [],
        "fulltime": {
          "flags": [
            "cross_timezone",
            "use_holidays_moving"
          ],
          "fri": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "mon": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "sat": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "sun": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "thu": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "tue": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
          "wed": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        },
        "grouped_regions_names": [
          "Россия"
        ],
        "language": {
          "english": [],
          "french": [],
          "german": []
        },
        "mobile_operation_systems": [],
        "mobile_region": [],
        "mobile_vendors": [],
        "interests": [],
        "pads": [
          {
            "description": "Социальные сети и сервисы (Одноклассники.Ру, МойМир@Mail.Ru, Почта@Mail.ru и др.)",
            "eye_url": {
              "description": "Посмотреть на Одноклассниках",
              "id": 1,
              "url": "http://www.odnoklassniki.ru/target"
            },
            "id": 5206,
            "name": "social_abstract"
          }
        ],
        "paid": "all",
        "profession": [],
        "regions": [
          188
        ],
        "regions_names": [
          "Россия"
        ],
        "remarketing": [],
        "salary": [],
        "sex": "FMU",
        "thematics": [],
        "tree": [],
        "user_geo": null,
        "week_days": [
          "mon",
          "tue",
          "wed",
          "thu",
          "fri",
          "sat",
          "sun"
        ]
      },
      "updated": "2013-06-27 13:50:30",
      "url": "/api/v1/campaigns/334648.json"
    }


### Изменение параметров кампании
`POST /api/v1/campaigns/{campaign_id}.json`

Метод изменяет параметры рекламной кампанию, переданные в виде объекта
CampaignForm. В случае успешного изменения в ответе возвращается объект
CampaignForm с изменёнными параметрами.

#### Пример

HTTP-запрос:

    POST /api/v1/campaigns/334648.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Content-Length: 37
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:1PzH+pX15ItMRGv0KcKr/sQ+tak=

    {"title": "\u0442\u0435\u0441\u0442"}

Curl-запрос:

    curl \
    curl -d '{"name": "Тестовая кампания №42"}' \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:1PzH+pX15ItMRGv0KcKr/sQ+tak=' \
    'https://target-sandbox.mail.ru/api/v1/campaigns/334648.json'

Пример ответа:

    {
      "name": "Тестовая кампания №42",
      "status": "active",
      "system_status": "active"
    }


### Экспорт кампании в CSV
`GET /api/v1/campaigns/{campaign_id}.{extension}`

Экспорт рекламной кампании вместе со всеми объявлениями в формате CSV или
в виде ZIP-файла, содержащего помимо CSV-файла ещё и изображения
объявлений. Возможные значения `extension`: `csv` и `zip`.


### Импорт кампании из CSV
`POST /api/v1/import/campaigns.json`

Метод принимает на вход CSV-файл или ZIP-архив (CSV-файл с описанием
рекламной кампании и объявлений вместе с файлами изображений). В случае
успешного разбора входных данных (если они корректны), метод возвращает
JSON-структуру типа CampaignForm, подходящую для отправки в метод создания
или обновления кампаний (`/api/v1/campaigns.json` или
`POST /api/v1/campaigns/{campaign_id}.json`).

