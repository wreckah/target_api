
## AuthToken

Токен для аутентификации в API.

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`access_id`</td>
            <td>`String`</td>
            <td>*64 символа*
<p>Идентификатор, передающийся в запросах в открытом виде</p></td>
        </tr><tr>
            <td>`private_key`</td>
            <td>`String`</td>
            <td>*64 символа*
<p>Секретный ключ для подписи запросов</p></td>
        </tr><tr>
            <td>`username`</td>
            <td>`String`</td>
            <td>*64 символа*
<p>Имя пользователя</p></td>
        </tr><tr>
            <td>`status`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Статус</p></td>
        </tr><tr>
            <td>`created`</td>
            <td>`DateTime`</td>
            <td><p>Дата и время создания</p></td>
        </tr>
    </tbody>
</table>