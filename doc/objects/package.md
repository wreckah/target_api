
## Package

Пакет услуг

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><p><code>id</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Идентификатор пакета</p></td>
        </tr><tr>
            <td><p><code>name</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Имя пакета</p></td>
        </tr><tr>
            <td><p><code>status</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em></p></td>
        </tr><tr>
            <td><p><code>system_status</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em></p></td>
        </tr><tr>
            <td><p><code>description</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Описание пакета</p></td>
        </tr><tr>
            <td><p><code>price_per_show</code></p></td>
            <td><p><code>Decimal</code></p></td>
            <td><p>Минимальная цена за показ</p></td>
        </tr><tr>
            <td><p><code>price_per_click</code></p></td>
            <td><p><code>Decimal</code></p></td>
            <td><p>Минимальна цена за клик</p></td>
        </tr><tr>
            <td><p><code>base_price_per_show</code></p></td>
            <td><p><code>Decimal</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>base_price_per_click</code></p></td>
            <td><p><code>Decimal</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>max_price_per_unit</code></p></td>
            <td><p><code>Decimal</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>highest_price_per_unit</code></p></td>
            <td><p><code>Decimal</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>eye_url</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>1024 символа</em></p></td>
        </tr><tr>
            <td><p><code>base_cpm_limit</code></p></td>
            <td><p><code>Decimal</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>features</code></p></td>
            <td><p>``</p></td>
            <td><p>Свойста пакета</p></td>
        </tr><tr>
            <td><p><code>banner_format</code></p></td>
            <td><p>``</p></td>
            <td><p>Формат баннера</p></td>
        </tr><tr>
            <td><p><code>targetings</code></p></td>
            <td><p><code>Targetings`</code>json
{
  "pads": "List"
}
```</p></td>
            <td><p>Доступные таргетинги</p></td>
        </tr><tr>
            <td><p><code>eye_urls</code></p></td>
            <td><p><code>[EyeUrls](eyeurl)</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>is_external</code></p></td>
            <td><p><code>Boolean</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>slider_positions</code></p></td>
            <td><p>``</p></td>
            <td></td>
        </tr><tr>
            <td><p><code>flags</code></p></td>
            <td><p><code>Strings</code></p></td>
            <td><p><em>255 символов</em></p></td>
        </tr>
    </tbody>
</table>