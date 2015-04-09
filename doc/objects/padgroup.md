
## PadGroup


<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>id</code></td>
            <td><code>Integer</code></td>
            <td></td>
        </tr><tr>
            <td><code>url</code></td>
            <td><code>String</code></td>
            <td><p><em>1024 символа</em> </p></td>
        </tr><tr>
            <td><code>description</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> </p></td>
        </tr><tr>
            <td><code>status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <em>active, deleted, blocked</em></p></td>
        </tr><tr>
            <td><code>platform</code></td>
            <td><a href="platform.md"><code>Platform</code></a></td>
            <td><p><em>Обязательный</em> </p></td>
        </tr><tr>
            <td><code>pads</code></td>
            <td>List of <a href="padforpadgroup.md"><code>PadForPadGroups</code></a></td>
            <td></td>
        </tr><tr>
            <td><code>moderation_status</code></td>
            <td><code>String</code></td>
            <td><p><em>255 символов</em> <br />Статус модерации</p></td>
        </tr><tr>
            <td><code>moderation_reason_display</code></td>
            <td><code>String</code></td>
            <td><p><em>1024 символа</em> <br />Причина модерации</p></td>
        </tr>
    </tbody>
</table>