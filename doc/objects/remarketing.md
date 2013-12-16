
## Remarketing

Ремаркетинговая аудитория позволяет показывать объявления тем
пользователям, которые ранее совершали определённые действия.

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Уникальный целочисленный идентификатор</p></td>
        </tr><tr>
            <td><code>name</code></td>
            <td><code>String</code></td>
            <td><p><em>Обязательный</em> <em>255 символов</em> <br />Название аудитории</p></td>
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
  "remarketing_groups": "List",
  "remarketing_users_lists": "List",
  "remarketing_context_phrases": "List"
}
```
</td>
            <td><p><br />Список таргетингов аудитории, которые срабатывают по
принципу «хотя бы один» (логическая дизъюнкция). Каждый из элементов списка
позволяет указать, в свою очередь, от одного до пяти таргетингов, которые
срабатывают по принципу «каждый» (логическая конъюнкция):</p>
<ul>
<li><code>remarketing_context_phrases</code> — посетители искавшие заданные фразы из ранее загруженного списка
в виде списка объектов <a href="#object_remarketingcontextphrases">RemarketingContextPhrases</a>;</li>
<li><code>remarketing_counters</code> — посетители на основании данных ремаркетинговых
счётчиков в виде списка объектов <a href="#object_remarketingcounterinterval">RemarketingCounterInterval</a>;</li>
<li><code>remarketing_game_payers</code> — посетители, платившие за приложение в соцсетях
<a href="http://my.mail.ru">Мой Мир</a> и <a href="http://odnoklassniki.ru/">Одноклассники</a>,
в виде списка объектов <a href="#object_remarketinggameinterval">RemarketingGameInterval</a>;</li>
<li><code>remarketing_game_players</code> — посетители, пользовавшиеся приложением в
соцсетях <a href="http://my.mail.ru">Мой Мир</a> и
<a href="http://odnoklassniki.ru/">Одноклассники</a>, в виде списка объектов
<a href="#object_remarketinggameinterval">RemarketingGameInterval</a>;</li>
<li><code>remarketing_payers</code> — посетители, в принципе платившие в приложениях
соцсетей Мой Мир и Одноклассники, в виде списка объектов
<a href="#object_remarketinginterval">RemarketingInterval</a>;</li>
<li><code>remarketing_payers</code> — посетители, в принципе пользовавшиеся приложениями
соцсетей Мой Мир и Одноклассники, в виде списка объектов
<a href="#object_remarketinginterval">RemarketingInterval</a>;</li>
<li><code>remarketing_group</code> — посетители, являющиеся участниками групп в соцсети
<a href="http://odnoklassniki.ru/">Одноклассники</a>, в виде списка объектов
<a href="#object_remarketinggroupmembership">RemarketingGroupMembership</a>.</li>
<li><code>remarketing_users_list</code> — посетители входящие в загруженные списки
в виде списка объектов <a href="#object_remarketinguserslist">RemarketingUsersList</a></li>
</ul></td>
        </tr><tr>
            <td><code>campaigns</code></td>
            <td>List of <code>Campaigns</code>
```json
{
  "id": "Integer, Идентификатор кампании",
  "name": "String, Название кампании",
  "edit_url": "String",
  "status": "String, Статус кампании"
}
```
</td>
            <td><p><br />Список рекламных кампаний, в которых используется аудитория</p></td>
        </tr>
    </tbody>
</table>