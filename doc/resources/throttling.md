## Информация по лимитам использования API


### Лимиты использования АПИ
`GET /api/v1/throttling.json`

Метод возвращает количество возможных запросов за разные промежутки времени и сколько запросов осталось
до конца периода.

#### Пример

HTTP-запрос:

    GET /api/v1/throttling.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Accept-Encoding: gzip, deflate, compress
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18

Curl-запрос:

    curl \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
    'https://target-sandbox.mail.ru/api/v1/throttling.json'

Пример ответа:

    {
      "CAMPAIGN": {
        "CREATE": {
          "limits": {"daily": 86400, "hourly": 3600, "rps": 1},
          "remaining": {"daily": 70000, "hourly": 1500, "rps": 0}
        },
        "READ": {
          "limits": {"daily": 86400, "hourly": 3600, "rps": 1},
          "remaining": {"daily": 70000, "hourly": 1500, "rps": 0}
        },
        "UPDATE": {
          "limits": {"daily": 86400, "hourly": 3600, "rps": 1},
          "remaining": {"daily": 70000, "hourly": 1500, "rps": 0}
        },
        "DELETE": {
          "limits": {"daily": 86400, "hourly": 3600, "rps": 1},
          "remainings": {"daily": 70000, "hourly": 1500, "rps": 0}
        }
      "BANNER": {
        "CREATE": {
          "limits": {"daily": 86400, "hourly": 3600, "rps": 1},
          "remaining": {"daily": 70000, "hourly": 1500, "rps": 0}
        },
        "READ": {
          "limits": {"daily": 86400, "hourly": 3600, "rps": 1},
          "remaining": {"daily": 70000, "hourly": 1500, "rps": 0}
        },
        "UPDATE": {
          "limits": {"daily": 86400, "hourly": 3600, "rps": 1},
          "remaining": {"daily": 70000, "hourly": 1500, "rps": 0}
        },
        "DELETE": {
          "limits": {"daily": 86400, "hourly": 3600, "rps": 1},
          "remaining": {"daily": 70000, "hourly": 1500, "rps": 0}
        }
      }
    }

