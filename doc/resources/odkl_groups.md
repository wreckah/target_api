## Группы в Одноклассниках
Группы в соцсети
[Одноклассники](http://odnoklassniki.ru/)

### Получение списка групп
`GET /api/v1/odkl_groups.json`

<p>Метод позволяет получить список групп соцсети
<a href="http://odnoklassniki.ru/">Одноклассники</a> в виде объектов
<a href="#object_odklgroups">OdklGroups</a> для дальнейшего использования их в качестве источника
данных для ремаркетинга.</p>
<p>Список формируется в результате поиска групп по вхождению поисковой фразы
в название группы. Поисковая фраза задаётся GET-параметром <code>q</code>.
Ограничить количество результатов поиска можно GET-параметром <code>limit</code>.
Значение <code>limit</code> «по умолчанию» — 10. Максимальное значение — 100.</p>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>GET /api/v1/odkl_groups.json?q=mail.ru HTTP/1.1
Host: target-sandbox.mail.ru
Content-Type: application/json
Accept-Encoding: gzip, deflate, compress
Authorization: AuthHMAC 9dEOYqb3sEmwKG9:A2m1j3ogy9fT0Ww+qb8/X2KhwgU=
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl \
-H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:A2m1j3ogy9fT0Ww+qb8/X2KhwgU=' \
'https://target-sandbox.mail.ru/api/v1/odkl_groups.json?q=mail.ru'
</code></pre>
<p>Пример ответа:</p>
<pre><code>[
  {
    "id": 53669865652234,
    "title": "agent@mail.ru"
  },
  {
    "id": 53708832309250,
    "title": "Mail.Ru Games"
  },
  {
    "id": 43065395314877,
    "title": "Mail.Ru Group"
  },
  ...
]
</code></pre>
