
## Campaign

Ресурс для создания/модификации рекламной кампании

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Идентификатор кампании</p></td>
        </tr><tr>
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><p><em>100 символов</em> <br />Название кампании</p></td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>active, deleted, blocked</em><br />Статус кампании</p></td>
        </tr><tr>
            <td><code>system_status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>active, deleted, blocked</em></p></td>
        </tr><tr>
            <td><code>created</code></td>
            <td><code>DateTime</code></td>
            <td><p><br />Время создания</p></td>
        </tr><tr>
            <td><code>updated</code></td>
            <td><code>DateTime</code></td>
            <td><p><br />Время последнего обновления</p></td>
        </tr><tr>
            <td><code>date_start</code></td>
            <td><code>Date</code></td>
            <td><p><br />Время старта кампании</p></td>
        </tr><tr>
            <td><code>date_end</code></td>
            <td><code>Date</code></td>
            <td><p><br />Время окончания кампании</p></td>
        </tr><tr>
            <td><code>package</code></td>
            <td><a href="package.md"><code>Package</code></a></td>
            <td><p><br />Структура пакета</p></td>
        </tr><tr>
            <td><code>price_per_show</code></td>
            <td><code>Decimal</code></td>
            <td><p><br />Цена за показ в рублях</p></td>
        </tr><tr>
            <td><code>price_per_click</code></td>
            <td><code>Decimal</code></td>
            <td><p><br />Цена за клик в рублях</p></td>
        </tr><tr>
            <td><code>budget_limit_day</code></td>
            <td><code>String</code></td>
            <td><p><em>32 символа</em> <br />Бюджет кампании на день</p></td>
        </tr><tr>
            <td><code>budget_limit</code></td>
            <td><code>String</code></td>
            <td><p><em>32 символа</em> <br />Общий бюджет кампании</p></td>
        </tr><tr>
            <td><code>mixing</code></td>
            <td><code>String</code></td>
            <td><p><em>64 символа</em> <em>fastest, recommended</em><br />Распределение бюджета</p></td>
        </tr><tr>
            <td><code>targetings</code></td>
            <td><a href="campaigntargetings.md"><code>CampaignTargetings</code></a></td>
            <td><p><br />Структура таргетингов</p></td>
        </tr><tr>
            <td><code>url</code></td>
            <td><code>String</code></td>
            <td><p><em>1024 символа</em> </p></td>
        </tr><tr>
            <td><code>edit_url</code></td>
            <td><code>String</code></td>
            <td><p><em>1024 символа</em> </p></td>
        </tr><tr>
            <td><code>banners_url</code></td>
            <td><code>String</code></td>
            <td><p><em>1024 символа</em> </p></td>
        </tr><tr>
            <td><code>banners_count</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Число баннеров в кампании</p></td>
        </tr><tr>
            <td><code>group_members</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> </p></td>
        </tr><tr>
            <td><code>autobidding_mode</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>fixed, second_price, second_price_mean</em><br />Аукционная стратегия</p></td>
        </tr><tr>
            <td><code>append_utm</code></td>
            <td><code>Boolean</code></td>
            <td><p><br />Deprecated</p></td>
        </tr><tr>
            <td><code>age_restrictions</code></td>
            <td><code>String</code></td>
            <td><p><em>3 символа</em> <br />Возрастные ограничения</p></td>
        </tr><tr>
            <td><code>pricelist</code></td>
            <td>partial <a href="remarketingpricelist.md"><code>RemarketingPricelist</code></a><br />
(<code>id</code>)
</td>
            <td></td>
        </tr><tr>
            <td><code>banners</code></td>
            <td>List of <a href="banner.md"><code>Banners</code></a></td>
            <td></td>
        </tr><tr>
            <td><code>last_updated</code></td>
            <td><code>DateTime</code></td>
            <td><p><br />Время последнего изменения (включая баннеры)</p></td>
        </tr><tr>
            <td><code>extended_age</code></td>
            <td><code>Boolean</code></td>
            <td></td>
        </tr><tr>
            <td><code>extended_pads</code></td>
            <td><code>Boolean</code></td>
            <td><p><br />Транслировать объявления на всех площадках подходящего формата (по умолчанию включено)</p></td>
        </tr><tr>
            <td><code>enable_recombination</code></td>
            <td><code>Boolean</code></td>
            <td></td>
        </tr><tr>
            <td><code>enable_utm</code></td>
            <td><code>Boolean</code></td>
            <td><p><br />Добавлять ли UTM-метки в URL объявлений</p></td>
        </tr><tr>
            <td><code>utm</code></td>
            <td><code>Text</code></td>
            <td><p><br />UTM-метки для добавления в URL объявлений. Если не указаны и <code>enable_utm=true</code>, то метки будут формироваться автоматически.</p></td>
        </tr><tr>
            <td><code>uniq_shows_limit</code></td>
            <td><code></code></td>
            <td><p><br />Количество уникальных показов</p></td>
        </tr><tr>
            <td><code>uniq_shows_period</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Периоды для показов</p></td>
        </tr><tr>
            <td><code>banner_uniq_shows_limit</code></td>
            <td><code></code></td>
            <td><p><br />Количество уникальных показов для баннеров</p></td>
        </tr><tr>
            <td><code>audit_pixels</code></td>
            <td>List of <code>Strings</code></td>
            <td><p><em>255 символов</em> <br />Список урлов пикселей для внешней статистики</p></td>
        </tr><tr>
            <td><code>url_object_id</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />ID рекламируемого приложения</p></td>
        </tr>
    </tbody>
</table>