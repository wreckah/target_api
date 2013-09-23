
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
            <td><br />Уникальный целочисленный идентификатор</td>
        </tr><tr>
            <td><code>app_id</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Уникальный символьный или целочисленный идентификатор
приложения в соцсетях [Мой Мир](http://my.mail.ru) и
[Одноклассники](http://odnoklassniki.ru/). Например, 259003 (Мой Мир)
или shakhmaty (Одноклассники).</td>
        </tr><tr>
            <td><code>app_type</code></td>
            <td><code>String</code></td>
            <td><em>64 символа</em> <em>odkl_app, mir_app</em><br />Платформа приложения</td>
        </tr>
    </tbody>
</table>