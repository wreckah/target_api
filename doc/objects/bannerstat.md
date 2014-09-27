
## BannerStat

Объект со статистикой объявления

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Идентификатор объявления</p></td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>active, deleted, blocked</em><br />Статус</p></td>
        </tr><tr>
            <td><code>system_status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>active, deleted, blocked</em><br />Системный статус</p></td>
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
            <td><p><em>255 символов</em> <br />Статус модерации</p></td>
        </tr><tr>
            <td><code>title</code></td>
            <td><code>AllowedChars</code></td>
            <td><p><em>255 символов</em> <br />Заголовок объявления</p></td>
        </tr><tr>
            <td><code>text</code></td>
            <td><code>AllowedChars</code></td>
            <td><p><em>90 символов</em> <br />Текст объявления</p></td>
        </tr><tr>
            <td><code>telephone</code></td>
            <td><code>String</code></td>
            <td><p><em>64 символа</em> <br />Номер телефона</p></td>
        </tr><tr>
            <td><code>company_name</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Название компании</p></td>
        </tr><tr>
            <td><code>url</code></td>
            <td><code>URL</code></td>
            <td><p><em>1024 символа</em> <br />Ссылка в объявлении</p></td>
        </tr><tr>
            <td><code>url_types</code></td>
            <td><code>Strings</code></td>
            <td><p><em>255 символов</em> <br />Типы ссылки</p></td>
        </tr><tr>
            <td><code>json_url</code></td>
            <td><code>String</code></td>
            <td><p><em>1024 символа</em> </p></td>
        </tr><tr>
            <td><code>edit_url</code></td>
            <td><code>String</code></td>
            <td><p><em>1024 символа</em> </p></td>
        </tr><tr>
            <td><code>preview_image_url</code></td>
            <td><code>String</code></td>
            <td><p><em>1024 символа</em> </p></td>
        </tr><tr>
            <td><code>user</code></td>
            <td><code>String</code><code>partial User</code><br />
(id)
</td>
            <td><p><br />Пользователь-владелец объявления</p></td>
        </tr><tr>
            <td><code>campaign</code></td>
            <td><code>String</code><code>partial User</code><br />
(id)
<code>partial CampaignBase</code><br />
(id, url)
</td>
            <td><p><br />Кампания объявления</p></td>
        </tr><tr>
            <td><code>category</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Категория объявления</p></td>
        </tr><tr>
            <td><code>moderation_reason_display</code></td>
            <td><code>String</code></td>
            <td><p><em>1024 символа</em> <br />Причина модерации</p></td>
        </tr><tr>
            <td><code>banner_moderation</code></td>
            <td><code>[BannerModeration](bannermoderation)</code></td>
            <td></td>
        </tr><tr>
            <td><code>image</code></td>
            <td><code>[Image](image)</code></td>
            <td><p><br />Изображение, отображающееся в объявлении</p></td>
        </tr><tr>
            <td><code>promo_image</code></td>
            <td><code>[Image](image)</code></td>
            <td><p><br />Большое изображение, отображающееся в объявлении</p></td>
        </tr><tr>
            <td><code>banner_fields</code></td>
            <td><code>Strings</code></td>
            <td><p><em>255 символов</em> </p></td>
        </tr><tr>
            <td><code>ctr_status</code></td>
            <td><code>String</code></td>
            <td><p><em>60 символов</em> <br />CTR-статус</p></td>
        </tr><tr>
            <td><code>stats</code></td>
            <td><code>[PeriodStat](periodstat)</code></td>
            <td><p><br />Статистика за всё время</p></td>
        </tr><tr>
            <td><code>stats_today</code></td>
            <td><code>[PeriodStat](periodstat)</code></td>
            <td><p><br />Статистика за сегодняшний день</p></td>
        </tr><tr>
            <td><code>stats_yesterday</code></td>
            <td><code>[PeriodStat](periodstat)</code></td>
            <td><p><br />Статистика за вчерашний день</p></td>
        </tr><tr>
            <td><code>stats_full</code></td>
            <td><code>[PeriodStats](periodstat)</code></td>
            <td><p><br />Статистика за последние 2 недели</p></td>
        </tr>
    </tbody>
</table>