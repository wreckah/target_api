
## Campaign

Объект создания/модификации кампании

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><br />Идентификатор кампании</td>
        </tr><tr>
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><em>40 символов</em> <br />Имя кампании</td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <em>active, deleted, blocked</em></td>
        </tr><tr>
            <td><code>system_status</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <em>active, deleted, blocked</em></td>
        </tr><tr>
            <td><code>created</code></td>
            <td><code>DateTime</code></td>
            <td><br />Время создания</td>
        </tr><tr>
            <td><code>updated</code></td>
            <td><code>DateTime</code></td>
            <td><br />Время последнего обновления</td>
        </tr><tr>
            <td><code>date_start</code></td>
            <td><code>Date</code></td>
            <td><br />Время старта кампании</td>
        </tr><tr>
            <td><code>date_end</code></td>
            <td><code>Date</code></td>
            <td><br />Время окончания кампании</td>
        </tr><tr>
            <td><code>package</code></td>
            <td><code>[Package](package)</code></td>
            <td><br />Структура пакета</td>
        </tr><tr>
            <td><code>price_per_show</code></td>
            <td><code>Decimal</code></td>
            <td><br />Цена за показ в рублях</td>
        </tr><tr>
            <td><code>price_per_click</code></td>
            <td><code>Decimal</code></td>
            <td><br />Цена за клик в рублях</td>
        </tr><tr>
            <td><code>budget_limit_day</code></td>
            <td><code>String</code></td>
            <td><em>32 символа</em> <br />Бюджет кампании на день</td>
        </tr><tr>
            <td><code>budget_limit</code></td>
            <td><code>String</code></td>
            <td><em>32 символа</em> <br />Общий бюджет кампании</td>
        </tr><tr>
            <td><code>mixing</code></td>
            <td><code>String</code></td>
            <td><em>64 символа</em> </td>
        </tr><tr>
            <td><code>targetings</code></td>
            <td><code>String</code><code>CampaignTargetings</code>
```json
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
}
```
</td>
            <td><br />Структура таргетингов</td>
        </tr><tr>
            <td><code>url</code></td>
            <td><code>String</code></td>
            <td><em>1024 символа</em> </td>
        </tr><tr>
            <td><code>edit_url</code></td>
            <td><code>String</code></td>
            <td><em>1024 символа</em> </td>
        </tr><tr>
            <td><code>banners_url</code></td>
            <td><code>String</code></td>
            <td><em>1024 символа</em> </td>
        </tr><tr>
            <td><code>banners_count</code></td>
            <td><code>Integer</code></td>
            <td><br />Число баннеров в кампании</td>
        </tr><tr>
            <td><code>gamers</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> </td>
        </tr><tr>
            <td><code>group_members</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> </td>
        </tr><tr>
            <td><code>autobidding_mode</code></td>
            <td><code>String</code></td>
            <td><em>255 символов</em> <br />Аукционная стратегия</td>
        </tr><tr>
            <td><code>append_utm</code></td>
            <td><code>Boolean</code></td>
            <td></td>
        </tr><tr>
            <td><code>slider_positions</code></td>
            <td><code></code></td>
            <td></td>
        </tr><tr>
            <td><code>banners</code></td>
            <td><code>[Banners](banner)</code></td>
            <td></td>
        </tr><tr>
            <td><code>last_updated</code></td>
            <td><code>DateTime</code></td>
            <td><br />Время последнего изменения (включая баннеры)</td>
        </tr><tr>
            <td><code>stats</code></td>
            <td><code>[PeriodStat](periodstat)</code></td>
            <td></td>
        </tr><tr>
            <td><code>stats_today</code></td>
            <td><code>[PeriodStat](periodstat)</code></td>
            <td></td>
        </tr><tr>
            <td><code>stats_yesterday</code></td>
            <td><code>[PeriodStat](periodstat)</code></td>
            <td></td>
        </tr><tr>
            <td><code>stats_full</code></td>
            <td><code>[PeriodStats](periodstat)</code></td>
            <td><br />Статистика за последние 2 недели</td>
        </tr><tr>
            <td><code>last_stats_updated</code></td>
            <td><code>DateTime</code></td>
            <td><br />Время последней статистики</td>
        </tr><tr>
            <td><code>extended_age</code></td>
            <td><code>Boolean</code></td>
            <td></td>
        </tr>
    </tbody>
</table>