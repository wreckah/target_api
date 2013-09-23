
## Remarketing

Ремаркетинговая аудитория позволяет показывать объявления тем
пользователям, которые уже посещали ваш сайт ранее.

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><br />Уникальный целочисленный идентификатор</td>
        </tr><tr>
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><em>Обязательный</em> <em>255 символов</em> <br />Название аудитории</td>
        </tr><tr>
            <td><code>disjunctions</code></td>
            <td>List of <code>Targetings</code>
```json
{
  "remarketing_counters": "List",
  "remarketing_game_payers": "List",
  "remarketing_game_players": "List",
  "remarketing_payers": "List",
  "remarketing_players": "List",
  "remarketing_groups": "List"
}
```
</td>
            <td><br />Список таргетингов аудитории, которые срабатывают по
принципу «хотя бы один» (логическая дизъюнкция). Каждый из элементов списка
позволяет указать, в свою очередь, от одного до пяти таргетингов, которые
срабатывают по принципу «каждый» (логическая конъюнкция):

* `remarketing_counters` — посетители на основании данных ремаркетинговых
счётчиков в виде списка объектов targeting.RemarketingCounterIntervalForm;
* `remarketing_game_payers` — посетители, платившие за приложение в соцсетях
[Мой Мир](http://my.mail.ru) и [Одноклассники](http://odnoklassniki.ru/),
в виде списка объектов targeting.RemarketingGameIntervalForm;
* `remarketing_game_players` — посетители, пользовавшиеся приложением в
соцсетях [Мой Мир](http://my.mail.ru) и
[Одноклассники](http://odnoklassniki.ru/), в виде списка объектов
targeting.RemarketingGameIntervalForm;
* `remarketing_payers` — посетители, в принципе платившие в приложениях
соцсетей Мой Мир и Одноклассники, в виде списка объектов
targeting.RemarketingIntervalForm;
* `remarketing_payers` — посетители, в принципе пользовавшиеся приложениями
соцсетей Мой Мир и Одноклассники, в виде списка объектов
targeting.RemarketingIntervalForm;
* `remarketing_group` — посетители, являющиеся участниками групп в соцсети
[Одноклассники](http://odnoklassniki.ru/), в виде списка объектов
targeting.RemarketingGroupMembershipForm.</td>
        </tr><tr>
            <td><code>campaigns</code></td>
            <td>List of <code>Campaigns</code>
```json
{
  "id": "Integer, Идентификатор кампании",
  "name": "String, Имя кампании",
  "edit_url": "String",
  "status": "String"
}
```
</td>
            <td><br />Список рекламных кампаний, в которых используется аудитория</td>
        </tr>
    </tbody>
</table>