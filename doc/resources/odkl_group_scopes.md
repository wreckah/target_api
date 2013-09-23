## Тематики групп в Одноклассниках
Тематики групп в соцсети
[Одноклассники](http://odnoklassniki.ru/)

### Получение списка тематик групп
`GET /api/v1/odkl_group_scopes.json`

<p>Метод позволяет получить список тематик групп соцсети
<a href="http://odnoklassniki.ru/">Одноклассники</a> в виде объектов
<a href="#object_odklgroupscope">OdklGroupScope</a> для дальнейшего использования их в качестве источника
данных для ремаркетинга.</p>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>GET /api/v1/odkl_group_scopes.json HTTP/1.1
Host: target-sandbox.mail.ru
Content-Type: application/json
Accept-Encoding: gzip, deflate, compress
Authorization: AuthHMAC 9dEOYqb3sEmwKG9:obZYc8pJH+Y1a9SFOHUptSHvaxE=
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl \
-H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:obZYc8pJH+Y1a9SFOHUptSHvaxE=' \
'https://target-sandbox.mail.ru/api/v1/odkl_group_scopes.json'
</code></pre>
<p>Пример ответа:</p>
<pre><code>[
  {
    "id": 9,
    "name": "Авто и мото"
  },
  ...
  {
    "id": 3,
    "name": "Игры"
  },
  ...
  {
    "id": 0,
    "name": "Музыка"
  },
  ...
]
</code></pre>
