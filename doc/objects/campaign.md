
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
            <td><p><br />Идентификатор кампании</p></td>
        </tr><tr>
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><p><em>40 символов</em> <br />Имя кампании</p></td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>active, deleted, blocked</em></p></td>
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
            <td><p><em>64 символа</em> <em>fastest, recommended</em><br />Распределение бюджета:</p>
<ul>
<li><code>default</code> — рекомендуемое;</li>
<li><code>fastest</code> — быстрое.</li>
</ul></td>
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
            <td><code>gamers</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> </p></td>
        </tr><tr>
            <td><code>group_members</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> </p></td>
        </tr><tr>
            <td><code>autobidding_mode</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>fixed, second_price, second_price_mean</em><br />Аукционная стратегия:</p>
<ul>
<li>Фиксированная ставка, <code>fixed</code> — переходы будут оплачиваться по указанной
  ставке, независимо от конкурентной ситуации</li>
<li>Минимальный расход, <code>second_price</code> — указывается максимальная ставка, если
  позволяет конкуренция, сервис автоматически её понижает;</li>
<li>Максимальное число переходов, <code>second_price_mean</code> — указывается средняя
  ставка, сервис обеспечит максимальное число переходов.</li>
</ul></td>
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
            <td><p><br />Время последнего изменения (включая баннеры)</p></td>
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
            <td><p><br />Статистика за последние 2 недели</p></td>
        </tr><tr>
            <td><code>last_stats_updated</code></td>
            <td><code>DateTime</code></td>
            <td><p><br />Время последней статистики</p></td>
        </tr><tr>
            <td><code>extended_age</code></td>
            <td><code>Boolean</code></td>
            <td></td>
        </tr><tr>
            <td><code>extended_pads</code></td>
            <td><code>Boolean</code></td>
            <td><p><br />Транслировать объявления на всех площадках подходящего формата (по умолчанию включено)</p></td>
        </tr>
    </tbody>
</table>