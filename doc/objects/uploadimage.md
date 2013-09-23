
## UploadImage

Параметры загрузки изображения

<table>
    <thead>
        <tr><th>Параметр</th><th>Тип</th><th>Значение</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><p><code>width</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Длина изображения (нужно указывать не размер исходного
изображения, а значение из свойства banner_format пакета, в рамках
которого будет создано объявление, использующее это изображение</p></td>
        </tr><tr>
            <td><p><code>height</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Высота изображения (пара <code>width</code> и <code>height</code> или
<code>banner_format_id</code> являются обязательными)</p></td>
        </tr><tr>
            <td><p><code>banner_format_id</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Идентификатор формата объявлений (вместо длины и высоты изображения можно указать его)</p></td>
        </tr><tr>
            <td><p><code>x1</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Координата X верхнего левого угла для кропа исходного
изображения</p></td>
        </tr><tr>
            <td><p><code>x2</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Координата X нижнего правого угла для кропа</p></td>
        </tr><tr>
            <td><p><code>y1</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Координата Y верхнего левого угла для кропа</p></td>
        </tr><tr>
            <td><p><code>y2</code></p></td>
            <td><p><code>Integer</code></p></td>
            <td><p>Координата Y нижнего правого угла для кропа</p></td>
        </tr><tr>
            <td><p><code>rollover</code></p></td>
            <td><p><code>Boolean</code></p></td>
            <td><p>Позволяет создать спойлер для анимированных изображений</p></td>
        </tr>
    </tbody>
</table>