## Биллинг


### Перевод денег от агентства клиенту и наоборот
`POST /api/v1/transactions/{mode}/{user_id}.json`

<p>Метод переводит деньги от агентства клиенту и наоборот. Параметры передаются
в виде объекта <a href="#object_agencydeposit">AgencyDeposit</a>. Параметры:</p>
<ul>
<li><code>mode</code>:<ul>
<li><code>from</code> — возврат со счета клиента на счет агентства;</li>
<li><code>to</code> — перевод со счета агентства на счет клиента;</li>
</ul>
</li>
<li><code>user_id</code> — целочисленный идентификатор клиентского пользователя или его
логин вида <code>username@mail.ru</code>.</li>
</ul>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>POST /api/v1/transactions/to/username@mail.ru.json HTTP/1.1
Host: target-sandbox.mail.ru
Content-Type: application/json
Content-Length: 19
Authorization: AuthHMAC 9dEOYqb3sEmwKG9:hViM17RQNg1Izv8pwmmZktMkoHQ=

{"amount": "10000"}
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl \
-d '{"amount": "10000"}' \
-H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:hViM17RQNg1Izv8pwmmZktMkoHQ=' \
'https://target-sandbox.mail.ru/api/v1/transactions/to/username@mail.ru.json'
</code></pre>
