
## CampaignTargetings


<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>pads</code></td>
            <td>List of <code>partial Pads</code><br />
(id, name, description, eye_url)
</td>
            <td><p><br />Рекламные площадки (для создания кампании достаточно передать только идентификаторы площадок)</p></td>
        </tr><tr>
            <td><code>remarketing</code></td>
            <td><code>[RemarketingTargetings](remarketingtargeting)</code></td>
            <td><p><br />Вхождение в аудитории</p></td>
        </tr><tr>
            <td><code>age</code></td>
            <td><code>Integers</code></td>
            <td><p><br />Возраст (список возрастов)</p></td>
        </tr><tr>
            <td><code>regions</code></td>
            <td><code>Integers</code></td>
            <td><p><br />Регионы (список идентификаторов регионов)</p></td>
        </tr><tr>
            <td><code>sex</code></td>
            <td><code>String</code></td>
            <td><p><em>3 символа</em> <br />Пол (сочетания <code>M</code> — мужской, <code>F</code> — женский, <code>U</code> — не указан)</p></td>
        </tr><tr>
            <td><code>fulltime</code></td>
            <td><code>[Fulltime](fulltime)</code></td>
            <td><p><br />Время (дни и часы)</p></td>
        </tr><tr>
            <td><code>education</code></td>
            <td><code>Strings</code></td>
            <td><p><em>255 символов</em> <br />Образование</p></td>
        </tr><tr>
            <td><code>salary</code></td>
            <td><code>Strings</code></td>
            <td><p><em>255 символов</em> <br />Диапазоны заработных плат</p></td>
        </tr><tr>
            <td><code>profession</code></td>
            <td><code>Strings</code></td>
            <td><p><em>255 символов</em> <br />Профессии</p></td>
        </tr><tr>
            <td><code>language</code></td>
            <td><code>[Language](language)</code></td>
            <td><p><br />Языки</p></td>
        </tr><tr>
            <td><code>birthday</code></td>
            <td><code>[Birthday](birthday)</code></td>
            <td><p><br />День рождения</p></td>
        </tr><tr>
            <td><code>user_geo</code></td>
            <td><code>Dict</code></td>
            <td><p><br />Географическое положение, указанное пользователем</p></td>
        </tr><tr>
            <td><code>mobile_types</code></td>
            <td><code>Strings</code></td>
            <td><p><em>255 символов</em> <em>tablets, smartphones</em><br />Типы мобильных устройств</p></td>
        </tr><tr>
            <td><code>mobile_operation_systems</code></td>
            <td><code>Integers</code></td>
            <td><p><br />Мобильные операционные системы (список идентификаторов объектов <a href="#object_mobileoperationsystem">MobileOperationSystem</a>)</p></td>
        </tr><tr>
            <td><code>mobile_operators</code></td>
            <td><code>Integers</code></td>
            <td><p><br />Операторы мобильной связи (список идентификаторов объектов <a href="#object_mobileoperator">MobileOperator</a>)</p></td>
        </tr><tr>
            <td><code>mobile_vendors</code></td>
            <td><code>Integers</code></td>
            <td><p><br />Производители мобильных устройств (список идентификаторов объектов <a href="#object_mobilevendor">MobileVendor</a>)</p></td>
        </tr><tr>
            <td><code>interests</code></td>
            <td><code>Integers</code></td>
            <td><p><br />Интересы пользователей</p></td>
        </tr>
    </tbody>
</table>