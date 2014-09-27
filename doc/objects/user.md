
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
            <td><code>permissions</code></td>
            <td><code></code></td>
            <td><p><br />Список прав пользователя</p></td>
        </tr><tr>
            <td><code>account</code></td>
            <td><code></code><code>partial UserAccount</code><br />
(id, balance, flags, type)
</td>
            <td><p><br />Информация о финансовом аккаунте пользователя</p></td>
        </tr><tr>
            <td><code>agency</code></td>
            <td><code></code><code>partial UserAccount</code><br />
(id, balance, flags, type)
<code>partial Agency</code><br />
(is_buyer, buyer_commission, overriding_commission)
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
        </tr><tr>
            <td><code>max_active_banners_count</code></td>
            <td><code>Integer</code></td>
            <td></td>
        </tr><tr>
            <td><code>active_banners_count</code></td>
            <td><code>Integer</code></td>
            <td></td>
        </tr><tr>
            <td><code>append_utm</code></td>
            <td><code>Boolean</code></td>
            <td><p><br />Признак простановки UTM-меток</p></td>
        </tr><tr>
            <td><code>show_compact_view</code></td>
            <td><code>Boolean</code></td>
            <td><p><br />Компактное представление страницы "Объявления"</p></td>
        </tr>
    </tbody>
</table>