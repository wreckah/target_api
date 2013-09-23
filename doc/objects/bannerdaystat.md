
## BannerDayStat

Статистические показатели объявления, агрегированные по дням.

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><br />Целочисленный идентификатор</td>
        </tr><tr>
            <td><code>total</code></td>
            <td><code>[BaseStat](basestat)</code></td>
            <td><br />Суммарная статистика за весь запрашиваемый период</td>
        </tr><tr>
            <td><code>detailed_stat</code></td>
            <td><code>[DateStats](datestat)</code></td>
            <td><br />Детализация статистики по запрашиваемому периоду</td>
        </tr><tr>
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Название</td>
        </tr>
    </tbody>
</table>