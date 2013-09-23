
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
            <td><p><em>64 символа</em> <br />Идентификатор, передающийся в запросах в открытом виде</p></td>
        </tr><tr>
            <td><code>private_key</code></td>
            <td><code>String</code></td>
            <td><p><em>64 символа</em> <br />Секретный ключ для подписи запросов</p></td>
        </tr><tr>
            <td><code>username</code></td>
            <td><code>String</code></td>
            <td><p><em>64 символа</em> <br />Имя пользователя</p></td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Статус</p></td>
        </tr><tr>
            <td><code>created</code></td>
            <td><code>DateTime</code></td>
            <td><p><br />Дата и время создания</p></td>
        </tr>
    </tbody>
</table>