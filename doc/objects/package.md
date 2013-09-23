
## Package

Пакет услуг

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Идентификатор пакета</p></td>
        </tr><tr>
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Имя пакета</p></td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> </p></td>
        </tr><tr>
            <td><code>system_status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> </p></td>
        </tr><tr>
            <td><code>description</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Описание пакета</p></td>
        </tr><tr>
            <td><code>price_per_show</code></td>
            <td><code>Decimal</code></td>
            <td><p><br />Минимальная цена за показ</p></td>
        </tr><tr>
            <td><code>price_per_click</code></td>
            <td><code>Decimal</code></td>
            <td><p><br />Минимальна цена за клик</p></td>
        </tr><tr>
            <td><code>base_price_per_show</code></td>
            <td><code>Decimal</code></td>
            <td></td>
        </tr><tr>
            <td><code>base_price_per_click</code></td>
            <td><code>Decimal</code></td>
            <td></td>
        </tr><tr>
            <td><code>max_price_per_unit</code></td>
            <td><code>Decimal</code></td>
            <td></td>
        </tr><tr>
            <td><code>highest_price_per_unit</code></td>
            <td><code>Decimal</code></td>
            <td></td>
        </tr><tr>
            <td><code>eye_url</code></td>
            <td><code>String</code></td>
            <td><p><em>1024 символа</em> </p></td>
        </tr><tr>
            <td><code>base_cpm_limit</code></td>
            <td><code>Decimal</code></td>
            <td></td>
        </tr><tr>
            <td><code>features</code></td>
            <td><code></code></td>
            <td><p><br />Свойста пакета</p></td>
        </tr><tr>
            <td><code>banner_format</code></td>
            <td><code></code></td>
            <td><p><br />Формат баннера</p></td>
        </tr><tr>
            <td><code>targetings</code></td>
            <td><code></code><code>Targetings</code>
```json
{
  "pads": "List"
}
```
</td>
            <td><p><br />Доступные таргетинги</p></td>
        </tr><tr>
            <td><code>eye_urls</code></td>
            <td><code>[EyeUrls](eyeurl)</code></td>
            <td></td>
        </tr><tr>
            <td><code>is_external</code></td>
            <td><code>Boolean</code></td>
            <td></td>
        </tr><tr>
            <td><code>slider_positions</code></td>
            <td><code></code></td>
            <td></td>
        </tr><tr>
            <td><code>flags</code></td>
            <td><code>Strings</code></td>
            <td><p><em>255 символов</em> </p></td>
        </tr>
    </tbody>
</table>