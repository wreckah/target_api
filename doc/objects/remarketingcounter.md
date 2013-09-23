
## RemarketingCounter

Ремаркетинговый счётчик — источник данных для ремаркетинга на основании
посещаемости [top.mail.ru](http://top.mail.ru/).

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
            <td>`status`</td>
            <td>`String`</td>
            <td>*255 символов*
*active, deleted, blocked*
<p>Пользовательский статус (<code>active</code>, <code>blocked</code>, <code>deleted</code>). Если счётчик
на top.mail.ru удаляют или деактивируют, то этот статус принимает
соответствующее значение. Неактивный счётчик нельзя использовать при
создании ремаркетирговой аудитории.</p></td>
        </tr><tr>
            <td>`system_status`</td>
            <td>`String`</td>
            <td>*255 символов*
*active, deleted, blocked*
<p>Системный статус (<code>active</code>, <code>blocked</code>, <code>deleted</code>). Используется для
активации счётчика если его создатель не является владельцем
соответствующего счётчика на top.mail.ru. Неактивный счётчик нельзя
использовать при создании ремаркетирговой аудитории.</p></td>
        </tr><tr>
            <td>`name`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Название счётчика</p></td>
        </tr><tr>
            <td>`counter_id`</td>
            <td>`Integer`</td>
            <td><p>Уникальный целочисленный идентификатор счётчика в системе top.mail.ru</p></td>
        </tr><tr>
            <td>`goals`</td>
            <td>`Dicts`</td>
            <td><p>Цели счётчика</p></td>
        </tr>
    </tbody>
</table>