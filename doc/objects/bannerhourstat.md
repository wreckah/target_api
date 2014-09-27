
## BannerHourStat

Статистические показатели объявления, агрегированные по часам.

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Целочисленный идентификатор</p></td>
        </tr><tr>
            <td><code>total</code></td>
            <td><a href="basestat.md"><code>BaseStat</code></a></td>
            <td><p><br />Суммарная статистика за весь запрашиваемый период</p></td>
        </tr><tr>
            <td><code>detailed_stat</code></td>
            <td><a href="datehourstat.md"><code>DateHourStats</code></a></td>
            <td><p><br />Детализация статистики по запрашиваемому периоду</p></td>
        </tr><tr>
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Название</p></td>
        </tr>
    </tbody>
</table>