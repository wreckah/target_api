
## AgencyClient


<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><p><code>id</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Идентификатор пользователя</p></td>
        </tr><tr>
            <td><p><code>username</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Имя пользователя. Может не совпадать с email</p></td>
        </tr><tr>
            <td><p><code>firstname</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Имя</p></td>
        </tr><tr>
            <td><p><code>lastname</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Фамилия</p></td>
        </tr><tr>
            <td><p><code>email</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Email</p></td>
        </tr><tr>
            <td><p><code>types</code></p></td>
            <td><p><code>Strings</code></p></td>
            <td><p><em>255 символов</em>
Массив ролей пользователя</p></td>
        </tr><tr>
            <td><p><code>status</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Статус</p></td>
        </tr><tr>
            <td><p><code>additional_info</code></p></td>
            <td><p><code>[AdditionalUserInfo](additionaluserinfo)</code></p></td>
            <td><p>структура AdditionalUserInfo</p></td>
        </tr><tr>
            <td><p><code>mailings</code></p></td>
            <td><p><code>Strings</code></p></td>
            <td><p><em>255 символов</em>
<em>news, finance, event, moderation, other</em></p></td>
        </tr><tr>
            <td><p><code>permissions</code></p></td>
            <td><p>``</p></td>
            <td><p>Список прав пользователя</p></td>
        </tr><tr>
            <td><p><code>account</code></p></td>
            <td><p><code>``UserAccount</code>
    {
      "id": "Integer",
      "balance": "Decimal",
      "flags": "List"
    }</p></td>
            <td><p>Информация о финансовом аккаунте пользователя</p></td>
        </tr><tr>
            <td><p><code>agency</code></p></td>
            <td><p><code>``UserAccount</code>
    {
      "id": "Integer",
      "balance": "Decimal",
      "flags": "List"
    }
<code>Agency</code>
    {
      "is_buyer": "Boolean",
      "buyer_commission": "Decimal",
      "overriding_commission": "Decimal"
    }</p></td>
            <td><p>Информация о агентском аккаунте пользователя</p></td>
        </tr><tr>
            <td><p><code>agency_username</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Username родительского агентства, если таковое есть</p></td>
        </tr><tr>
            <td><p><code>branch_username</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Username родительского представительства, если таковое есть</p></td>
        </tr><tr>
            <td><p><code>bf</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>flags</code></p></td>
            <td><p><code>Strings</code></p></td>
            <td><p><em>255 символов</em></p></td>
        </tr><tr>
            <td><p><code>is_red_client</code></p></td>
            <td><p><code>Boolean</code></p></td>
            <td><p>Является ли пользователь 'красным' клиентом</p></td>
        </tr><tr>
            <td><p><code>is_msk_allowed</code></p></td>
            <td><p><code>Boolean</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>is_spb_allowed</code></p></td>
            <td><p><code>Boolean</code></p></td>
            <td></td>
        </tr>
    </tbody>
</table>