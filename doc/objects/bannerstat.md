
## BannerStat

Объект со статистикой объявления для списка кампаний

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><p><code>id</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Идентификатор баннера</p></td>
        </tr><tr>
            <td><p><code>status</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
<em>active, deleted, blocked</em>
Статус</p></td>
        </tr><tr>
            <td><p><code>system_status</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
<em>active, deleted, blocked</em>
Системный статус</p></td>
        </tr><tr>
            <td><p><code>created</code></p></td>
            <td><p><code>DateTime</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>updated</code></p></td>
            <td><p><code>DateTime</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>moderation_status</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Статус модерации</p></td>
        </tr><tr>
            <td><p><code>title</code></p></td>
            <td><p><code>AllowedChars</code></p></td>
            <td><p><em>255 символов</em>
Заголовок баннера</p></td>
        </tr><tr>
            <td><p><code>text</code></p></td>
            <td><p><code>AllowedChars</code></p></td>
            <td><p><em>90 символов</em>
Текст баннера</p></td>
        </tr><tr>
            <td><p><code>telephone</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>64 символа</em></p></td>
        </tr><tr>
            <td><p><code>company_name</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em></p></td>
        </tr><tr>
            <td><p><code>url</code></p></td>
            <td><p><code>URL</code></p></td>
            <td><p><em>1024 символа</em>
Ссылка в баннере</p></td>
        </tr><tr>
            <td><p><code>json_url</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>1024 символа</em></p></td>
        </tr><tr>
            <td><p><code>edit_url</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>1024 символа</em></p></td>
        </tr><tr>
            <td><p><code>preview_image_url</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>1024 символа</em></p></td>
        </tr><tr>
            <td><p><code>user</code></p></td>
            <td><p><code>String``User</code>
    {
      "id": "Integer, Идентификатор пользователя"
    }</p></td>
            <td><p>Пользователь-владелец баннера</p></td>
        </tr><tr>
            <td><p><code>campaign</code></p></td>
            <td><p><code>String``User</code>
    {
      "id": "Integer, Идентификатор пользователя"
    }
<code>CampaignBase</code>
    {
      "id": "Integer, Идентификатор кампании",
      "url": "String"
    }</p></td>
            <td><p>Кампания баннера</p></td>
        </tr><tr>
            <td><p><code>moderation_reason_display</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>1024 символа</em>
Причина модерации</p></td>
        </tr><tr>
            <td><p><code>banner_moderation</code></p></td>
            <td><p><code>[BannerModeration](bannermoderation)</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>image</code></p></td>
            <td><p><code>[Image](image)</code></p></td>
            <td><p>Структура изображения</p></td>
        </tr><tr>
            <td><p><code>banner_fields</code></p></td>
            <td><p><code>Strings</code></p></td>
            <td><p><em>255 символов</em></p></td>
        </tr><tr>
            <td><p><code>stats</code></p></td>
            <td><p><code>[PeriodStat](periodstat)</code></p></td>
            <td><p>Статистика за всё время</p></td>
        </tr><tr>
            <td><p><code>stats_today</code></p></td>
            <td><p><code>[PeriodStat](periodstat)</code></p></td>
            <td><p>Статистика за сегодняшний день</p></td>
        </tr><tr>
            <td><p><code>stats_yesterday</code></p></td>
            <td><p><code>[PeriodStat](periodstat)</code></p></td>
            <td><p>Статистика за вчерашний день</p></td>
        </tr><tr>
            <td><p><code>stats_full</code></p></td>
            <td><p><code>[PeriodStats](periodstat)</code></p></td>
            <td><p>Статистика за последние 2 недели</p></td>
        </tr><tr>
            <td><p><code>ctr_status</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>60 символов</em>
CTR-статус</p></td>
        </tr>
    </tbody>
</table>