
## BannerDayStat

Статистические показатели объявления, агрегированные по дням.

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><p><code>id</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Целочисленный идентификатор</p></td>
        </tr><tr>
            <td><p><code>total</code></p></td>
            <td><p><code>[BaseStat](basestat)</code></p></td>
            <td><p>Суммарная статистика за весь запрашиваемый период</p></td>
        </tr><tr>
            <td><p><code>detailed_stat</code></p></td>
            <td><p><code>[DateStats](datestat)</code></p></td>
            <td><p>Детализация статистики по запрашиваемому периоду</p></td>
        </tr><tr>
            <td><p><code>name</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Название</p></td>
        </tr>
    </tbody>
</table>