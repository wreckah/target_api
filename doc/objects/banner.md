
## Banner

Объект для создания/модификации объявления (баннера)

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><br />Идентификатор баннера</td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <em>active, deleted, blocked</em><br />Статус</td>
        </tr><tr>
            <td><code>system_status</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <em>active, deleted, blocked</em><br />Системный статус</td>
        </tr><tr>
            <td><code>created</code></td>
            <td><code>DateTime</code></td>
            <td></td>
        </tr><tr>
            <td><code>updated</code></td>
            <td><code>DateTime</code></td>
            <td></td>
        </tr><tr>
            <td><code>moderation_status</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Статус модерации</td>
        </tr><tr>
            <td><code>title</code></td>
            <td><code>AllowedChars</code></td>
            <td><em>255 символов</em> <br />Заголовок баннера</td>
        </tr><tr>
            <td><code>text</code></td>
            <td><code>AllowedChars</code></td>
            <td><em>90 символов</em> <br />Текст баннера</td>
        </tr><tr>
            <td><code>telephone</code></td>
            <td><code>String</code></td>
            <td><em>64 символа</em> </td>
        </tr><tr>
            <td><code>company_name</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> </td>
        </tr><tr>
            <td><code>url</code></td>
            <td><code>URL</code></td>
            <td><em>1024 символа</em> <br />Ссылка в баннере</td>
        </tr><tr>
            <td><code>json_url</code></td>
            <td><code>String</code></td>
            <td><em>1024 символа</em> </td>
        </tr><tr>
            <td><code>edit_url</code></td>
            <td><code>String</code></td>
            <td><em>1024 символа</em> </td>
        </tr><tr>
            <td><code>preview_image_url</code></td>
            <td><code>String</code></td>
            <td><em>1024 символа</em> </td>
        </tr><tr>
            <td><code>user</code></td>
            <td><code>String</code><code>User</code>
```json
{
  "id": "Integer, Идентификатор пользователя"
}
```
</td>
            <td><br />Пользователь-владелец баннера</td>
        </tr><tr>
            <td><code>campaign</code></td>
            <td><code>String</code><code>User</code>
```json
{
  "id": "Integer, Идентификатор пользователя"
}
```
<code>CampaignBase</code>
```json
{
  "id": "Integer, Идентификатор кампании",
  "url": "String"
}
```
</td>
            <td><br />Кампания баннера</td>
        </tr><tr>
            <td><code>moderation_reason_display</code></td>
            <td><code>String</code></td>
            <td><em>1024 символа</em> <br />Причина модерации</td>
        </tr><tr>
            <td><code>banner_moderation</code></td>
            <td><code>[BannerModeration](bannermoderation)</code></td>
            <td></td>
        </tr><tr>
            <td><code>image</code></td>
            <td><code>[Image](image)</code></td>
            <td><br />Структура изображения</td>
        </tr><tr>
            <td><code>banner_fields</code></td>
            <td><code>Strings</code></td>
            <td><em>255 символов</em> </td>
        </tr><tr>
            <td><code>stats</code></td>
            <td><code>[PeriodStat](periodstat)</code></td>
            <td><br />Статистика за всё время</td>
        </tr><tr>
            <td><code>stats_today</code></td>
            <td><code>[PeriodStat](periodstat)</code></td>
            <td><br />Статистика за сегодняшний день</td>
        </tr><tr>
            <td><code>stats_yesterday</code></td>
            <td><code>[PeriodStat](periodstat)</code></td>
            <td><br />Статистика за вчерашний день</td>
        </tr><tr>
            <td><code>stats_full</code></td>
            <td><code>[PeriodStats](periodstat)</code></td>
            <td><br />Статистика за последние 2 недели</td>
        </tr><tr>
            <td><code>ctr_status</code></td>
            <td><code>String</code></td>
            <td><em>60 символов</em> <br />CTR-статус</td>
        </tr>
    </tbody>
</table>