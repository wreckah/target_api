
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
            <td><p><br />Уникальный целочисленный идентификатор</p></td>
        </tr><tr>
            <td><code>type</code></td>
            <td><code>String</code></td>
            <td><p><em>Обязательный</em> <em>20 символов</em> <em>group, scope</em><br />Тип сущности: группа или тематика групп</p></td>
        </tr><tr>
            <td><code>object_id</code></td>
            <td><code>Integer</code></td>
            <td><p><em>Обязательный</em> <br />Уникальный целочисленный идентификатор
группы или тематики групп в соцсети
<a href="http://odnoklassniki.ru/">Одноклассники</a>. Например, 50476261114004
(<a href="http://www.odnoklassniki.ru/gruppa">Группы на Одноклассниках</a>) или 4
(тематика «спорт и активный отдых»).</p></td>
        </tr><tr>
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Название группы или тематики</p></td>
        </tr><tr>
            <td><code>users_count</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Охват</p></td>
        </tr>
    </tbody>
</table>