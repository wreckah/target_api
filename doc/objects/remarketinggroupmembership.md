
## RemarketingGroupMembership

Условие для ремаркетинга на основании данных о членстве в группе
(или группах по тематике) соцсети
[Одноклассники](http://odnoklassniki.ru/). Обязательно наличие только
одного (и только одного!) параметра: `group_id`, `scope_id`.

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>type</code></td>
            <td><code>String</code></td>
            <td><p><em>Обязательный</em> <em>255 символов</em> <em>positive, negative</em><br />Условие показа объявления (членство в группе)</p></td>
        </tr><tr>
            <td><code>group_id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Целочисленный идентификатор группы в соцсети
<a href="http://odnoklassniki.ru/">Одноклассники</a>.</p></td>
        </tr><tr>
            <td><code>scope_id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Целочисленный идентификатор тематики групп в соцсети
<a href="http://odnoklassniki.ru/">Одноклассники</a></p></td>
        </tr>
    </tbody>
</table>