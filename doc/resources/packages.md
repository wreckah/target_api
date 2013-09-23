## Пакеты услуг


### Список пакетов
`GET /api/v1/packages.json`

<p>Метод возвращает список пакетов (объектов типа <a href="#object_package">Package</a>), доступных
пользователю. Пакет — это набор характеристик услуг, предоставляемых
пользователю в рамках рекламных кампаний, созданных с указанием этого
пакета. Например, формат баннеров, набор площадок, на которых будут
показываться объявления, список доступных таргетингов. Подробный список
характеристик можно посмотреть в описании объекта <a href="#object_package">Package</a>.</p>
<p>Идентификатор пакета необходим при создании рекламной кампании.</p>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>GET /api/v1/packages.json HTTP/1.1
Host: target-sandbox.mail.ru
Content-Type: application/json
Accept-Encoding: gzip, deflate, compress
Authorization: AuthHMAC 9dEOYqb3sEmwKG9:m65W22YBk9B69Prc/u+AUl79EHs=
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl \
-H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:m65W22YBk9B69Prc/u+AUl79EHs=' \
'https://target-sandbox.mail.ru/api/v1/packages.json'
</code></pre>
<p>Пример ответа:</p>
<pre><code>[
  {
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
    "base_cpm_limit": "2.5",
    "base_price_per_click": "0",
    "base_price_per_show": "0.0015",
    "description": "Мой Мир: внутренние ссылки, показы",
    "eye_url": "http://my.mail.ru/community/targetmailru",
    "eye_urls": [
      {
        "description": "Посмотреть на Моем Мире",
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
        "+gamers",
        "-regions"
      ],
      "targetings_": [
        "gamers",
        "age",
        "grouped_regions_names",
        "pads",
        "birthday",
        "sex",
        "pad_type",
        "regions_names",
        "fulltime"
      ],
      "url_type": "mir_redirect"
    },
    "highest_price_per_unit": "1.5",
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
          "description": "Другие проекты",
          "eye_url": {
            "description": "Посмотреть на Моем Мире",
            "id": 2,
            "url": "http://my.mail.ru/community/targetmailru"
          },
          "id": 3002,
          "name": "mail_other_abstract"
        },
        {
          "description": "Профили",
          "eye_url": {
            "description": "Посмотреть на Моем Мире",
            "id": 2,
            "url": "http://my.mail.ru/community/targetmailru"
          },
          "id": 3003,
          "name": "mail_mir_abstract"
        },
        {
          "description": "Приложения",
          "eye_url": {
            "description": "Посмотреть на Моем Мире",
            "id": 2,
            "url": "http://my.mail.ru/community/targetmailru"
          },
          "id": 4080,
          "name": "mail_mir_apps"
        }
      ]
    }
  }
]
</code></pre>
