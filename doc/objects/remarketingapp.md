
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
            <td>`id`</td>
            <td>`Integer`</td>
            <td><p>Уникальный целочисленный идентификатор</p></td>
        </tr><tr>
            <td>`app_id`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Уникальный символьный или целочисленный идентификатор
приложения в соцсетях <a href="http://my.mail.ru">Мой Мир</a> и
<a href="http://odnoklassniki.ru/">Одноклассники</a>. Например, 259003 (Мой Мир)
или shakhmaty (Одноклассники).</p></td>
        </tr><tr>
            <td>`app_type`</td>
            <td>`String`</td>
            <td>*64 символа*
*odkl_app, mir_app*
<p>Платформа приложения</p></td>
        </tr>
    </tbody>
</table>