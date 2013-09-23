
## RemarketingCounter

Ремаркетинговый счётчик — источник данных для ремаркетинга на основании
посещаемости [top.mail.ru](http://top.mail.ru/).

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
            <td><p><code>status</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
<em>active, deleted, blocked</em>
Пользовательский статус (<code>active</code>, <code>blocked</code>, <code>deleted</code>). Если счётчик
на top.mail.ru удаляют или деактивируют, то этот статус принимает
соответствующее значение. Неактивный счётчик нельзя использовать при
создании ремаркетирговой аудитории.</p></td>
        </tr><tr>
            <td><p><code>system_status</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
<em>active, deleted, blocked</em>
Системный статус (<code>active</code>, <code>blocked</code>, <code>deleted</code>). Используется для
активации счётчика если его создатель не является владельцем
соответствующего счётчика на top.mail.ru. Неактивный счётчик нельзя
использовать при создании ремаркетирговой аудитории.</p></td>
        </tr><tr>
            <td><p><code>name</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Название счётчика</p></td>
        </tr><tr>
            <td><p><code>counter_id</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Уникальный целочисленный идентификатор счётчика в системе top.mail.ru</p></td>
        </tr><tr>
            <td><p><code>goals</code></p></td>
            <td><p><code>Dicts</code></p></td>
            <td><p>Цели счётчика</p></td>
        </tr>
    </tbody>
</table>