
## BannerDayStat

Статистические показатели объявления, агрегированные по дням.

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`id`</td>
            <td>`Integer`</td>
            <td><p>Целочисленный идентификатор</p></td>
        </tr><tr>
            <td>`total`</td>
            <td>`[BaseStat](basestat)`</td>
            <td><p>Суммарная статистика за весь запрашиваемый период</p></td>
        </tr><tr>
            <td>`detailed_stat`</td>
            <td>`[DateStats](datestat)`</td>
            <td><p>Детализация статистики по запрашиваемому периоду</p></td>
        </tr><tr>
            <td>`name`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Название</p></td>
        </tr>
    </tbody>
</table>