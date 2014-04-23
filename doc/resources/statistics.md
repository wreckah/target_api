## Статистика


### Получение статистики по кампаниям или отдельным объявлениям
`GET /api/v1/statistics/{object_type}/{object_id}/{stat_type}/{date_from}-{date_to}.json`

Метод позволяет получать статистику по показам и кликам как по кампаниям,
так и по отдельным объявлениям. Параметры:

* `object_type` — задаёт тип сущности:
    + `banners` — объявление (в ответе — объект BannerHourStatForm или
    BannerDayStatForm в зависимости от значения `stat_type`);
    + `campaigns` — кампания (в ответе — объект ObjectHourStatForm или
    ObjectDayStatForm);
* `object_id` — целочисленный идентификатор сущности;
* `stat_type` — тип агрегации:
    + `hour` — по часам;
    + `day` — по дням;
* `date_from` — начальная дата;
* `date_to` — конечная дата.

Фильтр по датам необязательный, формат дат `DD.MM.YYYY`.

Можно запросить статистику для нескольких сущностей в одном запросе,
перечислив их идентификаторы через точку с запятой (`;`). В этом случае
метод вернёт список объектов вместо одного.

#### Пример

Статистика по кампании с почасовой агрегацией без указания дат, HTTP-запрос:

    GET /api/v1/statistics/campaigns/334789/hour.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:84h5h8j+aQR1xC0CZvXILnv0bEE=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:84h5h8j+aQR1xC0CZvXILnv0bEE=' \
    'https://target-sandbox.mail.ru/api/v1/statistics/campaigns/334789/hour.json'

Пример ответа:

    {
      "detailed_stat": [
        {
          "amount": "795.00",
          "clicks": 159,
          "ctr": "0.24",
          "date": "31.07.2013 14:00",
          "shows": 63826
        },
        {
          "amount": "1020.00",
          "clicks": 204,
          "ctr": "0.60",
          "date": "31.07.2013 15:00",
          "shows": 33507
        },
        {
          "amount": "1225.00",
          "clicks": 245,
          "ctr": "0.70",
          "date": "31.07.2013 16:00",
          "shows": 34643
        },
        ...
      ],
      "id": 334789,
      "name": "Новая кампания 2013-07-29",
      "total": {
        "amount": "18150.00",
        "clicks": 3630,
        "ctr": "0.46",
        "shows": 781028
      }
    }

Статистика по кампании с агрегацией по дням и указанием дат, HTTP-запрос:

    GET /api/v1/statistics/campaigns/334789/day/01.08.2013-01.08.2013.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:84h5h8j+aQR1xC0CZvXILnv0bEE=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:84h5h8j+aQR1xC0CZvXILnv0bEE=' \
    'https://target-sandbox.mail.ru/api/v1/statistics/campaigns/334789/day/01.08.2013-01.08.2013.json'

Пример ответа:

    {
      "detailed_stat": [
        {
          "amount": "10000.00",
          "clicks": 2000,
          "ctr": "0.46",
          "date": "01.08.2013",
          "shows": 426587
        }
      ],
      "id": 334789,
      "name": "Новая кампания 2013-07-29",
      "total": {
        "amount": "18150.00",
        "clicks": 3630,
        "ctr": "0.46",
        "shows": 781028
      }
}

Статистика по объявлению с почасовой агрегацией и указанием дат, HTTP-запрос:

    GET /api/v1/statistics/banners/688264/hour/01.08.2013-01.08.2013.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:O2NdGLbT9RF5NYOu4RaWpe65EVc=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:O2NdGLbT9RF5NYOu4RaWpe65EVc=' \
    'https://target-sandbox.mail.ru/api/v1/statistics/banners/688264/hour/01.08.2013-01.08.2013.json'

Пример ответа:

    {
      "detailed_stat": [
        {
          "amount": "450.00",
          "clicks": 90,
          "ctr": "0.24",
          "date": "01.08.2013 00:00",
          "shows": 36484
        },
        {
          "amount": "540.00",
          "clicks": 108,
          "ctr": "0.30",
          "date": "01.08.2013 01:00",
          "shows": 35119
        },
        ...
      ],
      "id": 688264,
      "name": "Детройт",
      "total": {
        "amount": "18150.00",
        "clicks": 3630,
        "ctr": "0.46",
        "shows": 781028
      }
    }

Статистика по нескольким объявлениям с агрегацией по дням без указания дат, HTTP-запрос:

    GET /api/v1/statistics/banners/688264;688267/day.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:O2NdGLbT9RF5NYOu4RaWpe65EVc=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:O2NdGLbT9RF5NYOu4RaWpe65EVc=' \
    'https://target-sandbox.mail.ru/api/v1/statistics/banners/688264;688267/day.json'

Пример ответа:

    [
      {
        "detailed_stat": [
          {
            "amount": "8150.00",
            "clicks": 1630,
            "ctr": "0.45",
            "date": "31.07.2013",
            "shows": 354441
          },
          {
            "amount": "10000.00",
            "clicks": 2000,
            "ctr": "0.46",
            "date": "01.08.2013",
            "shows": 426587
          }
        ],
        "id": 688264,
        "name": "Детройт",
        "total": {
          "amount": "18150.00",
          "clicks": 3630,
          "ctr": "0.46",
          "shows": 781028
        }
      },
      {
        "detailed_stat": [],
        "id": 688267,
        "name": "Kertch",
        "total": {
          "amount": "0.00",
          "clicks": 0,
          "ctr": "0.00",
          "shows": 0
        }
      }
    ]


### Получение быстрой статистики
`GET /api/v1/statistics/faststat/{object_type}/{object_id}.json`

Метод позволяет получать быструю статистику по пользователям, кампаниям, баннерам.
Параметры:

* `object_type` — задаёт тип сущности:
    + `banners` — объявление;
    + `campaigns` — кампания;
    + `users` — пользователь;
* `object_id` — целочисленный идентификатор сущности;

Можно запросить статистику для нескольких сущностей в одном запросе,
перечислив их идентификаторы через точку с запятой (`;`).

#### Пример

HTTP-запрос:

    GET /api/v1/statistics/faststat/banners/688264;688267.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC Bv2BaJv95g68G39:QOlK2RvHmew/975t7uW3r6RZUGI=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC Bv2BaJv95g68G39:QOlK2RvHmew/975t7uW3r6RZUGI=' \
    'https://target-sandbox.mail.ru/api/v1/statistics/faststat/banners/688264;688267.json'

Пример ответа:

    {
      "banners": {

        "688264": {
            "timestamp": 1379939599,
            "total": {
                "clicks":  [12345],
                "shows":   [1234567],
                "uniques": [123456]
            },
            "daily": {
                "clicks":  [0,0,0,0,33,408,156],
                "shows":   [0,0,0,0,92195,723098,320861],
                "uniques": [0,0,0,0,56140,372031,188179],
                "deltas":  [0,0,0,0,56140,350024,171259]
            },
            "hourly": {
                // то же, по часам за 24 часа
            },
            "minutely": {
                // то же, по минутам за 60 минут
            }
        },
        "688267": {
                // по другим баннерам, ...
                }
        }
      "last_seen_msg_time": {
        "ago": 30,
        "timestamp": 1391421987,
        "string": "2014-02-03 14:06:27"
      }
    }


