## Клиентские токены
Клиентские токены для доступа к API позволяют агентствам осуществлять
операции от имени клиентов.

Чтобы пользоваться методами API по работе с клиентскими токенам, нужно
иметь статус агентства. В противном случае все методы всегда будут
возвращать 403-ю HTTP-ошибку. Статус агентства можно получить при
[регистрации](https://target.mail.ru/agency/), указав всю необходимую
информацию.

### Получение списка клиентских токенов
`GET /api/v1/client_auth_tokens.json`

Метод возвращает список токенов для клиентских аккаунтов вашего агентства в
виде объектов типа AuthTokenForm.

#### Пример

HTTP-запрос:

    GET /api/v1/client_auth_tokens.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC N7qN8bmGURbwWft:rFchXU5kbTEAVNDPss+0PPo5U1s=

Curl-запрос:

    curl \
    -H 'Authorization: AuthHMAC N7qN8bmGURbwWft:rFchXU5kbTEAVNDPss+0PPo5U1s=' \
    'https://target-sandbox.mail.ru/api/v1/client_auth_tokens.json'

Пример ответа:

    [
      {
        "access_id": "QOFr6NqxE41QZZJ",
        "created": "2013-07-11 17:07:13",
        "private_key": "fKN1D1oLImybeKF",
        "status": "active",
        "username": "kgorilla@mail.ru"
      }
    ]


### Создание токена для клиента
`POST /api/v1/client_auth_token_for/{username}.json`

Метод позволяет создать токен для доступа к API от имени клиента вашего
агентства. Параметр `username` задаёт клиентского пользователя (вида
`user@mail.ru`), для которого нужно создать токен. В случае успеха
возвращает объект типа AuthTokenForm, содержащий поля `access_id` и
`private_key`, необходимые для подписи запросов. В случае, если
пользователь с именем `username` не найден или не является клиентом вашего
агентства, метод вернёт 404-ю HTTP-ошибку.

Токен создаётся один для каждого клиента. Если вызвать метод повторно для
того же клиента, в ответе вернётся тот же самый токен.

#### Пример

HTTP-запрос:

    POST /api/v1/client_auth_token_for/kgorilla@mail.ru.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC N7qN8bmGURbwWft:baJIl3MHTMJiD3UMwrSBKRbeo8w=

Curl-запрос:

    curl -X POST \
    -H 'Authorization: AuthHMAC N7qN8bmGURbwWft:baJIl3MHTMJiD3UMwrSBKRbeo8w=' \
    'https://target-sandbox.mail.ru/api/v1/client_auth_token_for/kgorilla@mail.ru.json'

Пример ответа:

    {
      "access_id": "QOFr6NqxE41QZZJ",
      "created": "2013-07-11 17:07:13",
      "private_key": "fKN1D1oLImybeKF",
      "status": "active",
      "username": "kgorilla@mail.ru"
    }


### Блокировка клиентского токена
`POST /api/v1/client_auth_token_block/{username}.json`

Метод позволяет заблокировать токен клиента. Это означает, что все запросы,
подписанные этим токеном будут возвращать 403-ю HTTP ошибку. Разблокировать
токен можно вызовом API-метода создания токена.

В случае успеха метод вернёт объект типа AuthTokenForm, поле `status`
которого будет содержать значение `blocked`.

#### Пример

HTTP-запрос:

    POST /api/v1/client_auth_token_block/kgorilla@mail.ru.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Accept-Encoding: gzip, deflate, compress
    Authorization: AuthHMAC N7qN8bmGURbwWft:cIONK/gTqI9epD+z0iQJfMP0WCQ=

Curl-запрос:

    curl -X POST \
    -H 'Authorization: AuthHMAC N7qN8bmGURbwWft:cIONK/gTqI9epD+z0iQJfMP0WCQ=' \
    'https://target-sandbox.mail.ru/api/v1/client_auth_token_block/kgorilla@mail.ru.json'

Пример ответа:

    {
      "access_id": "QOFr6NqxE41QZZJ",
      "created": "2013-07-11 17:07:13",
      "private_key": "fKN1D1oLImybeKF",
      "status": "blocked",
      "username": "kgorilla@mail.ru"
    }

