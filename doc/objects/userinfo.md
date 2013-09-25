
## UserInfo

Объект для получения и обновления данных текущего пользователя

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Идентификатор пользователя</p></td>
        </tr><tr>
            <td><code>firstname</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Имя</p></td>
        </tr><tr>
            <td><code>lastname</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Фамилия</p></td>
        </tr><tr>
            <td><code>email</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Email</p></td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>active, deleted, blocked</em><br />Статус</p></td>
        </tr><tr>
            <td><code>additional_info</code></td>
            <td><code>[AdditionalUserInfo](additionaluserinfo)</code></td>
            <td><p><br />Объект <a href="#object_additionaluserinfo">AdditionalUserInfo</a></p></td>
        </tr><tr>
            <td><code>mailings</code></td>
            <td><code>Strings</code></td>
            <td><p><em>255 символов</em> <em>news, finance, event, moderation, other</em><br />Список рассылок, на которые подписан пользователь</p></td>
        </tr><tr>
            <td><code>account</code></td>
            <td><code>Strings</code><code>UserAccount</code>
```json
{
  "id": "Integer",
  "balance": "Decimal",
  "flags": "List"
}
```
</td>
            <td><p><br />Информация о финансовом аккаунте пользователя</p></td>
        </tr><tr>
            <td><code>agency</code></td>
            <td><code>Strings</code><code>UserAccount</code>
```json
{
  "id": "Integer",
  "balance": "Decimal",
  "flags": "List"
}
```
<code>Agency</code>
```json
{
  "is_buyer": "Boolean",
  "buyer_commission": "Decimal",
  "overriding_commission": "Decimal"
}
```
</td>
            <td><p><br />Информация о агентском аккаунте пользователя</p></td>
        </tr>
    </tbody>
</table>