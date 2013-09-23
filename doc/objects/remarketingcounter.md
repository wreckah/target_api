
## RemarketingCounter

Ремаркетинговый счётчик — источник данных для ремаркетинга на основании
посещаемости [top.mail.ru](http://top.mail.ru/).

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
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>active, deleted, blocked</em><br />Пользовательский статус (<code>active</code>, <code>blocked</code>, <code>deleted</code>). Если счётчик
на top.mail.ru удаляют или деактивируют, то этот статус принимает
соответствующее значение. Неактивный счётчик нельзя использовать при
создании ремаркетирговой аудитории.</p></td>
        </tr><tr>
            <td><code>system_status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>active, deleted, blocked</em><br />Системный статус (<code>active</code>, <code>blocked</code>, <code>deleted</code>). Используется для
активации счётчика если его создатель не является владельцем
соответствующего счётчика на top.mail.ru. Неактивный счётчик нельзя
использовать при создании ремаркетирговой аудитории.</p></td>
        </tr><tr>
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Название счётчика</p></td>
        </tr><tr>
            <td><code>counter_id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Уникальный целочисленный идентификатор счётчика в системе top.mail.ru</p></td>
        </tr><tr>
            <td><code>goals</code></td>
            <td><code>Dicts</code></td>
            <td><p><br />Цели счётчика</p></td>
        </tr>
    </tbody>
</table>