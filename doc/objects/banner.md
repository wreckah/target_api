
## Banner

Объект для создания/модификации объявления (баннера)

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`id`</td>
            <td>`Integer`</td>
            <td><p>Идентификатор баннера</p></td>
        </tr><tr>
            <td>`status`</td>
            <td>`String`</td>
            <td>*255 символов*
*active, deleted, blocked*
<p>Статус</p></td>
        </tr><tr>
            <td>`system_status`</td>
            <td>`String`</td>
            <td>*255 символов*
*active, deleted, blocked*
<p>Системный статус</p></td>
        </tr><tr>
            <td>`created`</td>
            <td>`DateTime`</td>
            <td></td>
        </tr><tr>
            <td>`updated`</td>
            <td>`DateTime`</td>
            <td></td>
        </tr><tr>
            <td>`moderation_status`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Статус модерации</p></td>
        </tr><tr>
            <td>`title`</td>
            <td>`AllowedChars`</td>
            <td>*255 символов*
<p>Заголовок баннера</p></td>
        </tr><tr>
            <td>`text`</td>
            <td>`AllowedChars`</td>
            <td>*90 символов*
<p>Текст баннера</p></td>
        </tr><tr>
            <td>`telephone`</td>
            <td>`String`</td>
            <td>*64 символа*
</td>
        </tr><tr>
            <td>`company_name`</td>
            <td>`String`</td>
            <td>*255 символов*
</td>
        </tr><tr>
            <td>`url`</td>
            <td>`URL`</td>
            <td>*1024 символа*
<p>Ссылка в баннере</p></td>
        </tr><tr>
            <td>`json_url`</td>
            <td>`String`</td>
            <td>*1024 символа*
</td>
        </tr><tr>
            <td>`edit_url`</td>
            <td>`String`</td>
            <td>*1024 символа*
</td>
        </tr><tr>
            <td>`preview_image_url`</td>
            <td>`String`</td>
            <td>*1024 символа*
</td>
        </tr><tr>
            <td>`user`</td>
            <td>`String``User`
```json
{
  "id": "Integer, Идентификатор пользователя"
}
```</td>
            <td><p>Пользователь-владелец баннера</p></td>
        </tr><tr>
            <td>`campaign`</td>
            <td>`String``User`
```json
{
  "id": "Integer, Идентификатор пользователя"
}
````CampaignBase`
```json
{
  "id": "Integer, Идентификатор кампании",
  "url": "String"
}
```</td>
            <td><p>Кампания баннера</p></td>
        </tr><tr>
            <td>`moderation_reason_display`</td>
            <td>`String`</td>
            <td>*1024 символа*
<p>Причина модерации</p></td>
        </tr><tr>
            <td>`banner_moderation`</td>
            <td>`[BannerModeration](bannermoderation)`</td>
            <td></td>
        </tr><tr>
            <td>`image`</td>
            <td>`[Image](image)`</td>
            <td><p>Структура изображения</p></td>
        </tr><tr>
            <td>`banner_fields`</td>
            <td>`Strings`</td>
            <td>*255 символов*
</td>
        </tr><tr>
            <td>`stats`</td>
            <td>`[PeriodStat](periodstat)`</td>
            <td><p>Статистика за всё время</p></td>
        </tr><tr>
            <td>`stats_today`</td>
            <td>`[PeriodStat](periodstat)`</td>
            <td><p>Статистика за сегодняшний день</p></td>
        </tr><tr>
            <td>`stats_yesterday`</td>
            <td>`[PeriodStat](periodstat)`</td>
            <td><p>Статистика за вчерашний день</p></td>
        </tr><tr>
            <td>`stats_full`</td>
            <td>`[PeriodStats](periodstat)`</td>
            <td><p>Статистика за последние 2 недели</p></td>
        </tr><tr>
            <td>`ctr_status`</td>
            <td>`String`</td>
            <td>*60 символов*
<p>CTR-статус</p></td>
        </tr>
    </tbody>
</table>