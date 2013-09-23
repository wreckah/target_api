
## User


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
            <td><code>username</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Имя пользователя. Может не совпадать с email</p></td>
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
            <td><code>types</code></td>
            <td><code>Strings</code></td>
            <td><p><em>255 символов</em> <br />Массив ролей пользователя</p></td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Статус</p></td>
        </tr><tr>
            <td><code>additional_info</code></td>
            <td><code>[AdditionalUserInfo](additionaluserinfo)</code></td>
            <td><p><br />структура AdditionalUserInfo</p></td>
        </tr><tr>
            <td><code>mailings</code></td>
            <td><code>Strings</code></td>
            <td><p><em>255 символов</em> <em>news, finance, event, moderation, other</em></p></td>
        </tr><tr>
            <td><code>permissions</code></td>
            <td><code></code></td>
            <td><p><br />Список прав пользователя</p></td>
        </tr><tr>
            <td><code>account</code></td>
            <td><code></code><code>UserAccount</code>
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
            <td><code></code><code>UserAccount</code>
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
        </tr><tr>
            <td><code>agency_username</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Username родительского агентства, если таковое есть</p></td>
        </tr><tr>
            <td><code>branch_username</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Username родительского представительства, если таковое есть</p></td>
        </tr><tr>
            <td><code>bf</code></td>
            <td><code>Integer</code></td>
            <td></td>
        </tr><tr>
            <td><code>flags</code></td>
            <td><code>Strings</code></td>
            <td><p><em>255 символов</em> </p></td>
        </tr>
    </tbody>
</table>