
## Remarketing

Ремаркетинговая аудитория позволяет показывать объявления тем
пользователям, которые уже посещали ваш сайт ранее.

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><p><code>id</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Уникальный целочисленный идентификатор</p></td>
        </tr><tr>
            <td><p><code>name</code></p></td>
            <td><p><code>String</code></p></td>
            <td><p><em>Обязательный</em>
<em>255 символов</em>
Название аудитории</p></td>
        </tr><tr>
            <td><p><code>disjunctions</code></p></td>
            <td><p><code>List of ``Targetings</code>
    {
      "remarketing_counters": "List",
      "remarketing_game_payers": "List",
      "remarketing_game_players": "List",
      "remarketing_payers": "List",
      "remarketing_players": "List",
      "remarketing_groups": "List"
    }</p></td>
            <td><p>Список таргетингов аудитории, которые срабатывают по
принципу «хотя бы один» (логическая дизъюнкция). Каждый из элементов списка
позволяет указать, в свою очередь, от одного до пяти таргетингов, которые
срабатывают по принципу «каждый» (логическая конъюнкция):</p>
<ul>
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
</ul></td>
        </tr><tr>
            <td><p><code>campaigns</code></p></td>
            <td><p><code>List of ``Campaigns</code>
    {
      "id": "Integer, Идентификатор кампании",
      "name": "String, Имя кампании",
      "edit_url": "String",
      "status": "String"
    }</p></td>
            <td><p>Список рекламных кампаний, в которых используется аудитория</p></td>
        </tr>
    </tbody>
</table>