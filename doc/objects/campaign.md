
## Campaign

Объект создания/модификации кампании

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><p><code>id</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Идентификатор кампании</p></td>
        </tr><tr>
            <td><p><code>name</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>40 символов</em>
Имя кампании</p></td>
        </tr><tr>
            <td><p><code>status</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
<em>active, deleted, blocked</em></p></td>
        </tr><tr>
            <td><p><code>system_status</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
<em>active, deleted, blocked</em></p></td>
        </tr><tr>
            <td><p><code>created</code></p></td>
            <td><p><code>DateTime</code></p></td>
            <td><p>Время создания</p></td>
        </tr><tr>
            <td><p><code>updated</code></p></td>
            <td><p><code>DateTime</code></p></td>
            <td><p>Время последнего обновления</p></td>
        </tr><tr>
            <td><p><code>date_start</code></p></td>
            <td><p><code>Date</code></p></td>
            <td><p>Время старта кампании</p></td>
        </tr><tr>
            <td><p><code>date_end</code></p></td>
            <td><p><code>Date</code></p></td>
            <td><p>Время окончания кампании</p></td>
        </tr><tr>
            <td><p><code>package</code></p></td>
            <td><p><code>[Package](package)</code></p></td>
            <td><p>Структура пакета</p></td>
        </tr><tr>
            <td><p><code>price_per_show</code></p></td>
            <td><p><code>Decimal</code></p></td>
            <td><p>Цена за показ в рублях</p></td>
        </tr><tr>
            <td><p><code>price_per_click</code></p></td>
            <td><p><code>Decimal</code></p></td>
            <td><p>Цена за клик в рублях</p></td>
        </tr><tr>
            <td><p><code>budget_limit_day</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>32 символа</em>
Бюджет кампании на день</p></td>
        </tr><tr>
            <td><p><code>budget_limit</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>32 символа</em>
Общий бюджет кампании</p></td>
        </tr><tr>
            <td><p><code>mixing</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>64 символа</em></p></td>
        </tr><tr>
            <td><p><code>targetings</code></p></td>
            <td><p><code>String``CampaignTargetings</code>
<code>json
{
  "pads": "List",
  "age": "IntegerList",
  "regions": "IntegerList",
  "regions_names": "List",
  "grouped_regions_names": "List",
  "sex": "String",
  "week_days": "List",
  "day_hours": "IntegerList",
  "education": "List",
  "salary": "List",
  "language": "Language",
  "profession": "List",
  "paid": "String",
  "birthday": "Birthday",
  "projects": "List",
  "tree": "IntegerList",
  "user_geo": "Dict",
  "fulltime": "Fulltime",
  "remarketing": "List",
  "current_game": "Boolean",
  "current_group": "Boolean",
  "gaming_paid": "String",
  "thematics": "IntegerList",
  "mobile_types": "List",
  "mobile_operation_systems": "IntegerList",
  "mobile_operators": "IntegerList",
  "mobile_vendors": "IntegerList",
  "phrases": "Dict",
  "binmask": ""
}</code></p></td>
            <td><p>Структура таргетингов</p></td>
        </tr><tr>
            <td><p><code>url</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>1024 символа</em></p></td>
        </tr><tr>
            <td><p><code>edit_url</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>1024 символа</em></p></td>
        </tr><tr>
            <td><p><code>banners_url</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>1024 символа</em></p></td>
        </tr><tr>
            <td><p><code>banners_count</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Число баннеров в кампании</p></td>
        </tr><tr>
            <td><p><code>gamers</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em></p></td>
        </tr><tr>
            <td><p><code>group_members</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em></p></td>
        </tr><tr>
            <td><p><code>autobidding_mode</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>255 символов</em>
Аукционная стратегия</p></td>
        </tr><tr>
            <td><p><code>append_utm</code></p></td>
            <td><p><code>Boolean</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>slider_positions</code></p></td>
            <td><p>``</p></td>
            <td></td>
        </tr><tr>
            <td><p><code>banners</code></p></td>
            <td><p><code>[Banners](banner)</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>last_updated</code></p></td>
            <td><p><code>DateTime</code></p></td>
            <td><p>Время последнего изменения (включая баннеры)</p></td>
        </tr><tr>
            <td><p><code>stats</code></p></td>
            <td><p><code>[PeriodStat](periodstat)</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>stats_today</code></p></td>
            <td><p><code>[PeriodStat](periodstat)</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>stats_yesterday</code></p></td>
            <td><p><code>[PeriodStat](periodstat)</code></p></td>
            <td></td>
        </tr><tr>
            <td><p><code>stats_full</code></p></td>
            <td><p><code>[PeriodStats](periodstat)</code></p></td>
            <td><p>Статистика за последние 2 недели</p></td>
        </tr><tr>
            <td><p><code>last_stats_updated</code></p></td>
            <td><p><code>DateTime</code></p></td>
            <td><p>Время последней статистики</p></td>
        </tr><tr>
            <td><p><code>extended_age</code></p></td>
            <td><p><code>Boolean</code></p></td>
            <td></td>
        </tr>
    </tbody>
</table>