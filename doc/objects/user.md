
## User


<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`id`</td>
            <td>`Integer`</td>
            <td><p>Идентификатор пользователя</p></td>
        </tr><tr>
            <td>`username`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Имя пользователя. Может не совпадать с email</p></td>
        </tr><tr>
            <td>`firstname`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Имя</p></td>
        </tr><tr>
            <td>`lastname`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Фамилия</p></td>
        </tr><tr>
            <td>`email`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Email</p></td>
        </tr><tr>
            <td>`types`</td>
            <td>`Strings`</td>
            <td>*255 символов*
<p>Массив ролей пользователя</p></td>
        </tr><tr>
            <td>`status`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Статус</p></td>
        </tr><tr>
            <td>`additional_info`</td>
            <td>`[AdditionalUserInfo](additionaluserinfo)`</td>
            <td><p>структура AdditionalUserInfo</p></td>
        </tr><tr>
            <td>`mailings`</td>
            <td>`Strings`</td>
            <td>*255 символов*
*news, finance, event, moderation, other*
</td>
        </tr><tr>
            <td>`permissions`</td>
            <td>``</td>
            <td><p>Список прав пользователя</p></td>
        </tr><tr>
            <td>`account`</td>
            <td>```UserAccount`
```json
{
  "id": "Integer",
  "balance": "Decimal",
  "flags": "List"
}
```</td>
            <td><p>Информация о финансовом аккаунте пользователя</p></td>
        </tr><tr>
            <td>`agency`</td>
            <td>```UserAccount`
```json
{
  "id": "Integer",
  "balance": "Decimal",
  "flags": "List"
}
````Agency`
```json
{
  "is_buyer": "Boolean",
  "buyer_commission": "Decimal",
  "overriding_commission": "Decimal"
}
```</td>
            <td><p>Информация о агентском аккаунте пользователя</p></td>
        </tr><tr>
            <td>`agency_username`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Username родительского агентства, если таковое есть</p></td>
        </tr><tr>
            <td>`branch_username`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Username родительского представительства, если таковое есть</p></td>
        </tr><tr>
            <td>`bf`</td>
            <td>`Integer`</td>
            <td></td>
        </tr><tr>
            <td>`flags`</td>
            <td>`Strings`</td>
            <td>*255 символов*
</td>
        </tr>
    </tbody>
</table>