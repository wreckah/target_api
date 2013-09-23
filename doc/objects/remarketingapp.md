
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
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Уникальный целочисленный идентификатор</p></td>
        </tr><tr>
            <td><code>app_id</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Уникальный символьный или целочисленный идентификатор
приложения в соцсетях <a href="http://my.mail.ru">Мой Мир</a> и
<a href="http://odnoklassniki.ru/">Одноклассники</a>. Например, 259003 (Мой Мир)
или shakhmaty (Одноклассники).</p></td>
        </tr><tr>
            <td><code>app_type</code></td>
            <td><code>String</code></td>
            <td><p><em>64 символа</em> <em>odkl_app, mir_app</em><br />Платформа приложения</p></td>
        </tr>
    </tbody>
</table>