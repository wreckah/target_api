## Клиентские токены
Клиентские токены для доступа к API позволяют агенствам осуществлять
операции от имени клиентов.

Чтобы пользоваться методами API по работе с клиентскими токенам, нужно
иметь статус агенства. В противном случае все методы всегда будут
возвращать 403-ю HTTP-ошибку. Статус агенства можно получить при
[регистрации](https://target.mail.ru/agency/), указав всю необходимую
информацию.

### Получение списка клиентских токенов
`GET /api/v1/client_auth_tokens.json`

<p>Метод возвращает список токенов для клиентских аккаунтов вашего агенства в
виде объектов типа <a href="#object_authtoken">AuthToken</a>.</p>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>GET /api/v1/client_auth_tokens.json HTTP/1.1
Host: target-sandbox.mail.ru
Content-Type: application/json
Accept-Encoding: gzip, deflate, compress
Authorization: AuthHMAC N7qN8bmGURbwWft:rFchXU5kbTEAVNDPss+0PPo5U1s=
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl \
-H 'Authorization: AuthHMAC N7qN8bmGURbwWft:rFchXU5kbTEAVNDPss+0PPo5U1s=' \
'https://target-sandbox.mail.ru/api/v1/client_auth_tokens.json'
</code></pre>
<p>Пример ответа:</p>
<pre><code>[
  {
    "access_id": "QOFr6NqxE41QZZJ",
    "created": "2013-07-11 17:07:13",
    "private_key": "fKN1D1oLImybeKF",
    "status": "active",
    "username": "kgorilla@mail.ru"
  }
]
</code></pre>

### Создание токена для клиента
`POST /api/v1/client_auth_token_for/{username}.json`

<p>Метод позволяет создать токен для доступа к API от имени клиента вашего
агенства. Параметр <code>username</code> задаёт клиентского пользователя (вида
<code>user@mail.ru</code>), для которого нужно создать токен. В случае успеха
возвращает объект типа <a href="#object_authtoken">AuthToken</a>, содержащий поля <code>access_id</code> и
<code>private_key</code>, необходимые для подписи запросов. В случае, если
пользователь с именем <code>username</code> не найден или не является клиентом вашего
агенства, метод вернёт 404-ю HTTP-ошибку.</p>
<p>Токен создаётся один для каждого клиента. Если вызвать метод повторно для
того же клиента, в ответе вернётся тот же самый токен.</p>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>POST /api/v1/client_auth_token_for/kgorilla@mail.ru.json HTTP/1.1
Host: target-sandbox.mail.ru
Content-Type: application/json
Accept-Encoding: gzip, deflate, compress
Authorization: AuthHMAC N7qN8bmGURbwWft:baJIl3MHTMJiD3UMwrSBKRbeo8w=
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl -X POST \
-H 'Authorization: AuthHMAC N7qN8bmGURbwWft:baJIl3MHTMJiD3UMwrSBKRbeo8w=' \
'https://target-sandbox.mail.ru/api/v1/client_auth_token_for/kgorilla@mail.ru.json'
</code></pre>
<p>Пример ответа:</p>
<pre><code>{
  "access_id": "QOFr6NqxE41QZZJ",
  "created": "2013-07-11 17:07:13",
  "private_key": "fKN1D1oLImybeKF",
  "status": "active",
  "username": "kgorilla@mail.ru"
}
</code></pre>

### Блокировка клиентского токена
`POST /api/v1/client_auth_token_block/{username}.json`

<p>Метод позволяет заблокировать токен клиента. Это означает, что все запросы,
подписанные этим токеном будут возвращать 403-ю HTTP ошибку. Разблокировать
токен можно вызовом API-метода создания токена.</p>
<p>В случае успеха метод вернёт объект типа <a href="#object_authtoken">AuthToken</a>, поле <code>status</code>
которого будет содержать значение <code>blocked</code>.</p>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>POST /api/v1/client_auth_token_block/kgorilla@mail.ru.json HTTP/1.1
Host: target-sandbox.mail.ru
Content-Type: application/json
Accept-Encoding: gzip, deflate, compress
Authorization: AuthHMAC N7qN8bmGURbwWft:cIONK/gTqI9epD+z0iQJfMP0WCQ=
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl -X POST \
-H 'Authorization: AuthHMAC N7qN8bmGURbwWft:cIONK/gTqI9epD+z0iQJfMP0WCQ=' \
'https://target-sandbox.mail.ru/api/v1/client_auth_token_block/kgorilla@mail.ru.json'
</code></pre>
<p>Пример ответа:</p>
<pre><code>{
  "access_id": "QOFr6NqxE41QZZJ",
  "created": "2013-07-11 17:07:13",
  "private_key": "fKN1D1oLImybeKF",
  "status": "blocked",
  "username": "kgorilla@mail.ru"
}
</code></pre>
