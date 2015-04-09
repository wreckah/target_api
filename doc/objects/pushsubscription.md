
## PushSubscription

Подписка.

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Идентификатор подписки</p></td>
        </tr><tr>
            <td><code>user</code></td>
            <td>partial <a href="user.md"><code>User</code></a><br />
(<code>id</code>)
</td>
            <td><p><br />Пользователь</p></td>
        </tr><tr>
            <td><code>resource</code></td>
            <td><code>String</code></td>
            <td><p><em>Обязательный</em> <em>25 символов</em> <em>BANNER, CAMPAIGN</em><br />Ресурс</p></td>
        </tr><tr>
            <td><code>resource_id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Id Ресурса</p></td>
        </tr><tr>
            <td><code>callback_url</code></td>
            <td><code>URL</code></td>
            <td><p><em>Обязательный</em> <em>1024 символа</em> <br />Адрес, куда будет отправлено уведомление о событии</p></td>
        </tr><tr>
            <td><code>created</code></td>
            <td><code>DateTime</code></td>
            <td><p><br />Дата и время создания подписки</p></td>
        </tr>
    </tbody>
</table>