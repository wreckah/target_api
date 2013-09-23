
## Package

Пакет услуг

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`id`</td>
            <td>`Integer`</td>
            <td><p>Идентификатор пакета</p></td>
        </tr><tr>
            <td>`name`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Имя пакета</p></td>
        </tr><tr>
            <td>`status`</td>
            <td>`String`</td>
            <td>*255 символов*
</td>
        </tr><tr>
            <td>`system_status`</td>
            <td>`String`</td>
            <td>*255 символов*
</td>
        </tr><tr>
            <td>`description`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Описание пакета</p></td>
        </tr><tr>
            <td>`price_per_show`</td>
            <td>`Decimal`</td>
            <td><p>Минимальная цена за показ</p></td>
        </tr><tr>
            <td>`price_per_click`</td>
            <td>`Decimal`</td>
            <td><p>Минимальна цена за клик</p></td>
        </tr><tr>
            <td>`base_price_per_show`</td>
            <td>`Decimal`</td>
            <td></td>
        </tr><tr>
            <td>`base_price_per_click`</td>
            <td>`Decimal`</td>
            <td></td>
        </tr><tr>
            <td>`max_price_per_unit`</td>
            <td>`Decimal`</td>
            <td></td>
        </tr><tr>
            <td>`highest_price_per_unit`</td>
            <td>`Decimal`</td>
            <td></td>
        </tr><tr>
            <td>`eye_url`</td>
            <td>`String`</td>
            <td>*1024 символа*
</td>
        </tr><tr>
            <td>`base_cpm_limit`</td>
            <td>`Decimal`</td>
            <td></td>
        </tr><tr>
            <td>`features`</td>
            <td>``</td>
            <td><p>Свойста пакета</p></td>
        </tr><tr>
            <td>`banner_format`</td>
            <td>``</td>
            <td><p>Формат баннера</p></td>
        </tr><tr>
            <td>`targetings`</td>
            <td>```Targetings`
```json
{
  "pads": "List"
}
```</td>
            <td><p>Доступные таргетинги</p></td>
        </tr><tr>
            <td>`eye_urls`</td>
            <td>`[EyeUrls](eyeurl)`</td>
            <td></td>
        </tr><tr>
            <td>`is_external`</td>
            <td>`Boolean`</td>
            <td></td>
        </tr><tr>
            <td>`slider_positions`</td>
            <td>``</td>
            <td></td>
        </tr><tr>
            <td>`flags`</td>
            <td>`Strings`</td>
            <td>*255 символов*
</td>
        </tr>
    </tbody>
</table>