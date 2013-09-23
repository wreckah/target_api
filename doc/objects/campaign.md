
## Campaign

Объект создания/модификации кампании

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`id`</td>
            <td>`Integer`</td>
            <td><p>Идентификатор кампании</p></td>
        </tr><tr>
            <td>`name`</td>
            <td>`String`</td>
            <td>*40 символов*
<p>Имя кампании</p></td>
        </tr><tr>
            <td>`status`</td>
            <td>`String`</td>
            <td>*255 символов*
*active, deleted, blocked*
</td>
        </tr><tr>
            <td>`system_status`</td>
            <td>`String`</td>
            <td>*255 символов*
*active, deleted, blocked*
</td>
        </tr><tr>
            <td>`created`</td>
            <td>`DateTime`</td>
            <td><p>Время создания</p></td>
        </tr><tr>
            <td>`updated`</td>
            <td>`DateTime`</td>
            <td><p>Время последнего обновления</p></td>
        </tr><tr>
            <td>`date_start`</td>
            <td>`Date`</td>
            <td><p>Время старта кампании</p></td>
        </tr><tr>
            <td>`date_end`</td>
            <td>`Date`</td>
            <td><p>Время окончания кампании</p></td>
        </tr><tr>
            <td>`package`</td>
            <td>`[Package](package)`</td>
            <td><p>Структура пакета</p></td>
        </tr><tr>
            <td>`price_per_show`</td>
            <td>`Decimal`</td>
            <td><p>Цена за показ в рублях</p></td>
        </tr><tr>
            <td>`price_per_click`</td>
            <td>`Decimal`</td>
            <td><p>Цена за клик в рублях</p></td>
        </tr><tr>
            <td>`budget_limit_day`</td>
            <td>`String`</td>
            <td>*32 символа*
<p>Бюджет кампании на день</p></td>
        </tr><tr>
            <td>`budget_limit`</td>
            <td>`String`</td>
            <td>*32 символа*
<p>Общий бюджет кампании</p></td>
        </tr><tr>
            <td>`mixing`</td>
            <td>`String`</td>
            <td>*64 символа*
</td>
        </tr><tr>
            <td>`targetings`</td>
            <td>`String``CampaignTargetings`
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
```</td>
            <td><p>Структура таргетингов</p></td>
        </tr><tr>
            <td>`url`</td>
            <td>`String`</td>
            <td>*1024 символа*
</td>
        </tr><tr>
            <td>`edit_url`</td>
            <td>`String`</td>
            <td>*1024 символа*
</td>
        </tr><tr>
            <td>`banners_url`</td>
            <td>`String`</td>
            <td>*1024 символа*
</td>
        </tr><tr>
            <td>`banners_count`</td>
            <td>`Integer`</td>
            <td><p>Число баннеров в кампании</p></td>
        </tr><tr>
            <td>`gamers`</td>
            <td>`String`</td>
            <td>*255 символов*
</td>
        </tr><tr>
            <td>`group_members`</td>
            <td>`String`</td>
            <td>*255 символов*
</td>
        </tr><tr>
            <td>`autobidding_mode`</td>
            <td>`String`</td>
            <td>*255 символов*
<p>Аукционная стратегия</p></td>
        </tr><tr>
            <td>`append_utm`</td>
            <td>`Boolean`</td>
            <td></td>
        </tr><tr>
            <td>`slider_positions`</td>
            <td>``</td>
            <td></td>
        </tr><tr>
            <td>`banners`</td>
            <td>`[Banners](banner)`</td>
            <td></td>
        </tr><tr>
            <td>`last_updated`</td>
            <td>`DateTime`</td>
            <td><p>Время последнего изменения (включая баннеры)</p></td>
        </tr><tr>
            <td>`stats`</td>
            <td>`[PeriodStat](periodstat)`</td>
            <td></td>
        </tr><tr>
            <td>`stats_today`</td>
            <td>`[PeriodStat](periodstat)`</td>
            <td></td>
        </tr><tr>
            <td>`stats_yesterday`</td>
            <td>`[PeriodStat](periodstat)`</td>
            <td></td>
        </tr><tr>
            <td>`stats_full`</td>
            <td>`[PeriodStats](periodstat)`</td>
            <td><p>Статистика за последние 2 недели</p></td>
        </tr><tr>
            <td>`last_stats_updated`</td>
            <td>`DateTime`</td>
            <td><p>Время последней статистики</p></td>
        </tr><tr>
            <td>`extended_age`</td>
            <td>`Boolean`</td>
            <td></td>
        </tr>
    </tbody>
</table>