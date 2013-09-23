
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
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><br />Уникальный целочисленный идентификатор</td>
        </tr><tr>
            <td><code>type</code></td>
            <td><code>String</code></td>
            <td><em>Обязательный</em> <em>20 символов</em> <em>group, scope</em><br />Тип сущности: группа или тематика групп</td>
        </tr><tr>
            <td><code>object_id</code></td>
            <td><code>Integer</code></td>
            <td><em>Обязательный</em> <br />Уникальный целочисленный идентификатор
группы или тематики групп в соцсети
[Одноклассники](http://odnoklassniki.ru/). Например, 50476261114004
([Группы на Одноклассниках](http://www.odnoklassniki.ru/gruppa)) или 4
(тематика «спорт и активный отдых»).</td>
        </tr><tr>
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Название группы или тематики</td>
        </tr>
    </tbody>
</table>