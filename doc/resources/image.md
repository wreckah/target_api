## Изображения


### Загрузка изображения для рекламного объявления
`POST /api/v1/images.json`

<p>Метод позволяет загрузить изображение для рекламного объявления. В случае
успешной загрузки он возвращает объект типа <a href="#object_image">Image</a>, который можно
использовать для создания рекламного объявления, передав его в свойстве
<code>image</code> объекта объявления «как есть». На данный момент поддерживаются
форматы JPEG, GIF, PNG, SWF.</p>
<p>Алгоритм подписи запроса на загрузку изображения немного отличается от
стандартного. В запросе необходимо передать HTTP-заголовок <code>X-Trg-Chksum</code>,
который содержит хэш-сумму от загружаемого изображения, полученную по
алгоритму <code>MD5</code>. Кроме того, при создании подписи вместо тела POST-запроса
нужно использовать эту же хэш-сумму.</p>
<p>В отличие от других POST-запросов к API, имеющих тип <code>application/json</code>,
запрос на загрузку изображения должен иметь тип <code>multipart/form-data</code>.
Само изображение для загрузки нужно передавать как часть multipart-запроса
с именем <code>image_file</code>. Параметры изображения нужно передавать также в
multipart-виде. Возможные параметры описывает объект <a href="#object_uploadimage">UploadImage</a>.
Пара параметров <code>width</code> и <code>height</code> или параметр <code>banner_format_id</code>
(идентификатор свойства banner_format пакета, в котором будет создано
объявления) являются обязательными для указания. Они задают размеры,
к которым будет приведено загружаемое изображение для отображения в
объявлении.</p>

#### Пример

<p>Для загрузки в примере используется <a href="https://limg.imgsmail.ru/s/images/logo/logo_wide.v2.png">изображение</a>.</p>
<p>HTTP-запрос:</p>
<pre><code>POST /api/v1/images.json HTTP/1.1
Host: target-sandbox.mail.ru
Content-Type: multipart/form-data; boundary=----------------------------284bab249df5
Content-Length: 1991
Accept-Encoding: gzip, deflate, compress
X-Trg-Chksum: 094c464e6d5666254ff123d60e618cbe
Authorization: AuthHMAC 9dEOYqb3sEmwKG9:Y68uooAYiSyzZeU/nMTiXA5mFkY=

------------------------------284bab249df5
Content-Disposition: form-data; name="width"

60
------------------------------284bab249df5
Content-Disposition: form-data; name="height"

15
------------------------------284bab249df5
Content-Disposition: form-data; name="image_file"; filename="logo_wide.v2.png"
Content-Type: application/octet-stream

&lt;бинарные данные файла-изображения&gt;
------------------------------284bab249df5--
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl -F width=60 -F height=15 -F image_file=@logo_wide.v2.png \
-H 'X-Trg-Chksum: 094c464e6d5666254ff123d60e618cbe' \
-H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:Y68uooAYiSyzZeU/nMTiXA5mFkY=' \
'https://target-sandbox.mail.ru/api/v1/images.json'
</code></pre>
<p>Пример ответа:</p>
<pre><code>{
  "height": 15,
  "id": 201206,
  "is_animated": false,
  "preview_url": "/upload_file/preview/http/r.mail.ru/img/5A/7A69E7.png?",
  "size": 1201,
  "type": "static",
  "url": "http://r.mail.ru/img/5A/7A69E7.png",
  "width": 60
}
</code></pre>
