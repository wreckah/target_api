
## RemarketingApp

Ремаркетинговое приложение — источник данных для ремаркетинга на
основании использования или оплаты приложений в соцсетях
[Мой Мир](http://my.mail.ru) и [Одноклассники](http://odnoklassniki.ru/).

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><p><code>id</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Уникальный целочисленный идентификатор</p></td>
        </tr><tr>
            <td><p><code>app_id</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Уникальный символьный или целочисленный идентификатор
приложения в соцсетях <a href="http://my.mail.ru">Мой Мир</a> и
<a href="http://odnoklassniki.ru/">Одноклассники</a>. Например, 259003 (Мой Мир)
или shakhmaty (Одноклассники).</p></td>
        </tr><tr>
            <td><p><code>app_type</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>64 символа</em>
<em>odkl_app, mir_app</em>
Платформа приложения</p></td>
        </tr>
    </tbody>
</table>