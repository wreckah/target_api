
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
            <td>`type`</td>
            <td>`String`</td>
            <td>*Обязательный*
*255 символов*
*positive, negative*
<p>Условие показа объявления (членство в группе)</p></td>
        </tr><tr>
            <td>`group_id`</td>
            <td>`Integer`</td>
            <td><p>Целочисленный идентификатор группы в соцсети
<a href="http://odnoklassniki.ru/">Одноклассники</a>.</p></td>
        </tr><tr>
            <td>`scope_id`</td>
            <td>`Integer`</td>
            <td><p>Целочисленный идентификатор тематики групп в соцсети
<a href="http://odnoklassniki.ru/">Одноклассники</a></p></td>
        </tr>
    </tbody>
</table>