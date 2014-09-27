
## CampaignBase

Базовая форма кампании

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
            <td><p><em>40 символов</em> <br />Название кампании</p></td>
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
            <td><code>[Package](package)</code></td>
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
            <td><code>[CampaignTargetings](campaigntargetings)</code></td>
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
            <td></td>
        </tr><tr>
            <td><code>age_restrictions</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>, 0+, 6+, 12+, 16+, 18+</em><br />Возрастные ограничения</p></td>
        </tr><tr>
            <td><code>pricelist</code></td>
            <td>partial <code>RemarketingPricelist</code><br />
(<code>id</code>)
</td>
            <td></td>
        </tr>
    </tbody>
</table>