
## RemarketingPricelist

Ремаркетинговый прайс-лист

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
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><p><em>Обязательный</em> <em>255 символов</em> <br />Название</p></td>
        </tr><tr>
            <td><code>export_url</code></td>
            <td><code>String</code></td>
            <td><p><em>Обязательный</em> <em>512 символов</em> <br />Ссылка на прайс-лист</p></td>
        </tr><tr>
            <td><code>shop_id</code></td>
            <td><code>Integer</code></td>
            <td><p><em>Обязательный</em> <br />Счетчик из ТОП</p></td>
        </tr><tr>
            <td><code>feed_id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Номер прайса внутри магазина</p></td>
        </tr><tr>
            <td><code>created</code></td>
            <td><code>DateTime</code></td>
            <td><p><br />Дата создания</p></td>
        </tr><tr>
            <td><code>last_import_finished</code></td>
            <td><code>DateTime</code></td>
            <td><p><br />Дата последней выгрузки</p></td>
        </tr>
    </tbody>
</table>