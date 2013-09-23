
## UploadImage

Параметры загрузки изображения

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><code>width</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Ширина изображения (нужно указывать не размер исходного
изображения, а значение из свойства banner_format пакета, в рамках
которого будет создано объявление, использующее это изображение</p></td>
        </tr><tr>
            <td><code>height</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Высота изображения (пара <code>width</code> и <code>height</code> или
<code>banner_format_id</code> являются обязательными)</p></td>
        </tr><tr>
            <td><code>banner_format_id</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Идентификатор формата объявлений (вместо ширины и высоты изображения можно указать его)</p></td>
        </tr><tr>
            <td><code>x1</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Координата X верхнего левого угла для кропа исходного
изображения</p></td>
        </tr><tr>
            <td><code>x2</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Координата X нижнего правого угла для кропа</p></td>
        </tr><tr>
            <td><code>y1</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Координата Y верхнего левого угла для кропа</p></td>
        </tr><tr>
            <td><code>y2</code></td>
            <td><code>Integer</code></td>
            <td><p><br />Координата Y нижнего правого угла для кропа</p></td>
        </tr><tr>
            <td><code>rollover</code></td>
            <td><code>Boolean</code></td>
            <td><p><br />Позволяет создать спойлер для анимированных изображений</p></td>
        </tr>
    </tbody>
</table>