
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
            <td><br />Длина изображения (нужно указывать не размер исходного
изображения, а значение из свойства banner_format пакета, в рамках
которого будет создано объявление, использующее это изображение</td>
        </tr><tr>
            <td><code>height</code></td>
            <td><code>Integer</code></td>
            <td><br />Высота изображения (пара `width` и `height` или
`banner_format_id` являются обязательными)</td>
        </tr><tr>
            <td><code>banner_format_id</code></td>
            <td><code>Integer</code></td>
            <td><br />Идентификатор формата объявлений (вместо длины и высоты изображения можно указать его)</td>
        </tr><tr>
            <td><code>x1</code></td>
            <td><code>Integer</code></td>
            <td><br />Координата X верхнего левого угла для кропа исходного
изображения</td>
        </tr><tr>
            <td><code>x2</code></td>
            <td><code>Integer</code></td>
            <td><br />Координата X нижнего правого угла для кропа</td>
        </tr><tr>
            <td><code>y1</code></td>
            <td><code>Integer</code></td>
            <td><br />Координата Y верхнего левого угла для кропа</td>
        </tr><tr>
            <td><code>y2</code></td>
            <td><code>Integer</code></td>
            <td><br />Координата Y нижнего правого угла для кропа</td>
        </tr><tr>
            <td><code>rollover</code></td>
            <td><code>Boolean</code></td>
            <td><br />Позволяет создать спойлер для анимированных изображений</td>
        </tr>
    </tbody>
</table>