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
    Authorization: AuthHMAC 9dEOYqb3sEmwKG9:hViM17RQNg1Izv8pwmmZktMkoHQ=

    {"amount": "10000"}

Curl-запрос:

    curl \
    -d '{"amount": "10000"}' \
    -H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:hViM17RQNg1Izv8pwmmZktMkoHQ=' \
    'https://target-sandbox.mail.ru/api/v1/transactions/to/username@mail.ru.json'



*Generated automatically at 2013-09-23 00:28:14.749368*