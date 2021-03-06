## Изображения


### Загрузка изображения для рекламного объявления
`POST /api/v1/images.json`

Метод позволяет загрузить изображение для рекламного объявления. В случае
успешной загрузки он возвращает объект типа ImageForm, который можно
использовать для создания рекламного объявления, передав его в свойстве
`image` объекта объявления «как есть». На данный момент поддерживаются
форматы JPEG, GIF, PNG, SWF.

В отличие от других POST-запросов к API, имеющих тип `application/json`,
запрос на загрузку изображения должен иметь тип `multipart/form-data`.
Само изображение для загрузки нужно передавать как часть multipart-запроса
с именем `image_file`. Параметры изображения нужно передавать также в
multipart-виде. Возможные параметры описывает объект UploadImageForm.
Пара параметров `width` и `height` или параметр `banner_format_id`
(идентификатор свойства banner_format пакета, в котором будет создано
объявления) являются обязательными для указания. Они задают размеры,
к которым будет приведено загружаемое изображение для отображения в
объявлении.

#### Пример

Для загрузки в примере используется [изображение](https://limg.imgsmail.ru/s/images/logo/logo_wide.v2.png).

HTTP-запрос:

    POST /api/v1/images.json HTTP/1.1
    Host: target-sandbox.my.com
    Content-Type: multipart/form-data; boundary=----------------------------284bab249df5
    Content-Length: 1991
    Accept-Encoding: gzip, deflate, compress
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18

    ------------------------------284bab249df5
    Content-Disposition: form-data; name="width"

    60
    ------------------------------284bab249df5
    Content-Disposition: form-data; name="height"

    15
    ------------------------------284bab249df5
    Content-Disposition: form-data; name="image_file"; filename="logo_wide.v2.png"
    Content-Type: application/octet-stream

    <бинарные данные файла-изображения>
    ------------------------------284bab249df5--

Curl-запрос:

    curl -F width=60 -F height=15 -F image_file=@logo_wide.v2.png \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
    'https://target-sandbox.my.com/api/v1/images.json'

Пример ответа:

    {
      "height": 15,
      "id": 201206,
      "is_animated": false,
      "preview_url": "/upload_file/preview/http/r.mail.ru/img/5A/7A69E7.png?",
      "size": 1201,
      "type": "static",
      "url": "http://r.mail.ru/img/5A/7A69E7.png",
      "width": 60
    }

