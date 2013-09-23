
## AuthToken

Токен для аутентификации в API.

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>access_id</code></td>
            <td><code>String</code></td>
            <td><em>64 символа</em> <br />Идентификатор, передающийся в запросах в открытом виде</td>
        </tr><tr>
            <td><code>private_key</code></td>
            <td><code>String</code></td>
            <td><em>64 символа</em> <br />Секретный ключ для подписи запросов</td>
        </tr><tr>
            <td><code>username</code></td>
            <td><code>String</code></td>
            <td><em>64 символа</em> <br />Имя пользователя</td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Статус</td>
        </tr><tr>
            <td><code>created</code></td>
            <td><code>DateTime</code></td>
            <td><br />Дата и время создания</td>
        </tr>
    </tbody>
</table>