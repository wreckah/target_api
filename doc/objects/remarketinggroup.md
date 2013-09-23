
## RemarketingGroup

Ремаркетинговая группа (или тематика) — источник данных для
ремаркетинга на основании участия посетителя в группах соцсети
[Одноклассники](http://odnoklassniki.ru/).

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
            <td><p><code>type</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>Обязательный</em>
<em>20 символов</em>
<em>group, scope</em>
Тип сущности: группа или тематика групп</p></td>
        </tr><tr>
            <td><p><code>object_id</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p><em>Обязательный</em>
Уникальный целочисленный идентификатор
группы или тематики групп в соцсети
<a href="http://odnoklassniki.ru/">Одноклассники</a>. Например, 50476261114004
(<a href="http://www.odnoklassniki.ru/gruppa">Группы на Одноклассниках</a>) или 4
(тематика «спорт и активный отдых»).</p></td>
        </tr><tr>
            <td><p><code>name</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Название группы или тематики</p></td>
        </tr>
    </tbody>
</table>