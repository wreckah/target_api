
## RemarketingMobileApps


<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>left</code></td>
            <td><code>Integer</code></td>
            <td><p><em>Обязательный</em> <br />Минимальное значение параметра для показа объявления (левая граница временного интервала, дней назад)</p></td>
        </tr><tr>
            <td><code>right</code></td>
            <td><code>Integer</code></td>
            <td><p><em>Обязательный</em> <br />Максимальное значение параметра для показа объявления (правая граница интервала временного интервала, дней назад)</p></td>
        </tr><tr>
            <td><code>type</code></td>
            <td><code>String</code></td>
            <td><p><em>Обязательный</em> <em>255 символов</em> <em>positive, negative</em><br />Условие показа объявления (попадание значения параметра в интервал, заданный <code>left</code> и <code>right</code>).</p></td>
        </tr><tr>
            <td><code>mobile_app_id</code></td>
            <td><code>Integer</code></td>
            <td><p><em>Обязательный</em> </p></td>
        </tr><tr>
            <td><code>install_type</code></td>
            <td><code>String</code></td>
            <td><p><em>Обязательный</em> <em>255 символов</em> <em>now, any_time, deleted</em><br />Условие показа</p></td>
        </tr>
    </tbody>
</table>