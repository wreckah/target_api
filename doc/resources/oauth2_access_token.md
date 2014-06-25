## Access-токен для OAuth2
Access-токен является неотъемлемой частью протокола
[OAuth2](http://tools.ietf.org/html/draft-ietf-oauth-v2-31), который
поддерживает API Target@Mail.Ru. Подробнее о реализации OAuth2 в
API читайте [тут](/doc/api/oauth2).

### Метод для операций с access-токеном для OAuth2
`POST /api/v2/oauth2/token.json`

Метод позволяет производить различные операции с access-токеном в
зависимости от параметра `grant_type`.

При `grant_type=authorization_code` метод создаёт новый access-токен по
коду гранта (параметр `code`), выданного пользователем в схеме
Authorization Code Grant протокола OAuth2.

При `grant_type=client_credentials` метод создаёт новый access-токен по
паре `client_id`, `client_secret`, получаемой при регистрации
OAuth-клиента. Это реализация схемы Client Credentials Grant протокола
OAuth2.

При `grant_type=refresh_token` метод создаёт новый access-токен взамен
старого, который идентифицируется переданным параметром `refresh_token`.

Вариант `grant_type=agency_client_credentials` не является стандартным для
OAuth2. Он реализован для того, чтобы агентства могли создавать
access-токены для своих клиентов напрямую. Помимо параметров `client_id`,
`client_secret` нужно передавать `agency_client_name`.

