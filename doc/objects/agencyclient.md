
## AgencyClient


<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><br />Идентификатор пользователя</td>
        </tr><tr>
            <td><code>username</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Имя пользователя. Может не совпадать с email</td>
        </tr><tr>
            <td><code>firstname</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Имя</td>
        </tr><tr>
            <td><code>lastname</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Фамилия</td>
        </tr><tr>
            <td><code>email</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Email</td>
        </tr><tr>
            <td><code>types</code></td>
            <td><code>Strings</code></td>
            <td><em>255 символов</em> <br />Массив ролей пользователя</td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Статус</td>
        </tr><tr>
            <td><code>additional_info</code></td>
            <td><code>[AdditionalUserInfo](additionaluserinfo)</code></td>
            <td><br />структура AdditionalUserInfo</td>
        </tr><tr>
            <td><code>mailings</code></td>
            <td><code>Strings</code></td>
            <td><em>255 символов</em> <em>news, finance, event, moderation, other</em></td>
        </tr><tr>
            <td><code>permissions</code></td>
            <td><code></code></td>
            <td><br />Список прав пользователя</td>
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
            <td><br />Информация о финансовом аккаунте пользователя</td>
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
            <td><br />Информация о агентском аккаунте пользователя</td>
        </tr><tr>
            <td><code>agency_username</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Username родительского агентства, если таковое есть</td>
        </tr><tr>
            <td><code>branch_username</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Username родительского представительства, если таковое есть</td>
        </tr><tr>
            <td><code>bf</code></td>
            <td><code>Integer</code></td>
            <td></td>
        </tr><tr>
            <td><code>flags</code></td>
            <td><code>Strings</code></td>
            <td><em>255 символов</em> </td>
        </tr><tr>
            <td><code>is_red_client</code></td>
            <td><code>Boolean</code></td>
            <td><br />Является ли пользователь 'красным' клиентом</td>
        </tr><tr>
            <td><code>is_msk_allowed</code></td>
            <td><code>Boolean</code></td>
            <td></td>
        </tr><tr>
            <td><code>is_spb_allowed</code></td>
            <td><code>Boolean</code></td>
            <td></td>
        </tr>
    </tbody>
</table>