
## AgencyClient


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
            <td><code>additional_info</code></td>
            <td><code>[AdditionalUserInfo](additionaluserinfo)</code></td>
            <td><p><br />Объект <a href="#object_additionaluserinfo">AdditionalUserInfo</a></p></td>
        </tr><tr>
            <td><code>account</code></td>
            <td><code>[AdditionalUserInfo](additionaluserinfo)</code><code>partial UserAccount</code><br />
(id, balance, flags, type)
</td>
            <td><p><br />Информация о финансовом аккаунте пользователя</p></td>
        </tr><tr>
            <td><code>is_red_client</code></td>
            <td><code>Boolean</code></td>
            <td><p><br />Является ли пользователь 'красным' клиентом</p></td>
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