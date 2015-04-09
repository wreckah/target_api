## Биллинг


### Перевод денег от агентства клиенту и наоборот
`POST /api/v1/transactions/{mode}/{user_id}.json`

Метод переводит деньги от агентства клиенту и наоборот. Параметры передаются
в виде объекта AgencyDepositForm. Параметры:

* `mode`:
    + `from` — возврат со счета клиента на счет агентства;
    + `to` — перевод со счета агентства на счет клиента;
* `user_id` — целочисленный идентификатор клиентского пользователя или его
логин вида `username@mail.ru`.

#### Пример

HTTP-запрос:

    POST /api/v1/transactions/to/username@mail.ru.json HTTP/1.1
    Host: target-sandbox.mail.ru
    Content-Type: application/json
    Content-Length: 19
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18

    {"amount": "10000"}

Curl-запрос:

    curl \
    -d '{"amount": "10000"}' \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
    'https://target-sandbox.mail.ru/api/v1/transactions/to/username@mail.ru.json'

