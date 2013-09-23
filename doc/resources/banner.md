## Рекламные объявления


### Получение информации об объявлении
`GET /api/v1/banners/{banner_id}.json`

<p>Метод возвращает полную информацию об объявлении в виде объекта
<a href="#object_bannerstat">BannerStat</a>. Возможно передать несколько значений <code>{banner_id}</code>,
разделённых точкой с запятой (<code>;</code>). В таком случае метод вернёт список
объектов <a href="#object_bannerstat">BannerStat</a>.</p>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>GET /api/v1/banners/687419.json HTTP/1.1
Host: target-sandbox.mail.ru
Accept-Encoding: gzip, deflate, compress
Authorization: AuthHMAC 9dEOYqb3sEmwKG9:SuIoHIpS7PXhc//eJFO+T0477/I=
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl \
-H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:SuIoHIpS7PXhc//eJFO+T0477/I=' \
'https://target-sandbox.mail.ru/api/v1/banners/687419.json'
</code></pre>
<p>Пример ответа:</p>
<pre><code>{
  "banner_fields": [
    "title",
    "text",
    "url",
    "image"
  ],
  "banner_moderation": {
    "moderation_comment": "",
    "moderation_reason": ""
  },
  "campaign": {
    "id": 334648,
    "url": "/api/v1/campaigns/334648.json"
  },
  "company_name": "",
  "created": "2013-06-27 13:50:09",
  "ctr_status": "bad_start_cpm",
  "edit_url": "/ads/banners/687419/edit/",
  "id": 687419,
  "image": {
    "height": 45,
    "id": 24513,
    "is_animated": false,
    "preview_url": "https://rb.mail.ru/img/BA/573CCB.jpg",
    "size": 1616,
    "type": "static",
    "url": "http://r.mail.ru/img/BA/573CCB.jpg",
    "width": 60
  },
  "json_url": "/api/v1/banners/687419.json",
  "moderation_reason_display": "",
  "moderation_status": "new",
  "preview_image_url": "https://rb.mail.ru/img/BA/573CCB.jpg",
  "stats": {
    "amount": "0.00",
    "clicks": 0,
    "shows": 0
  },
  "stats_today": {
    "amount": "0.00",
    "clicks": 0,
    "shows": 0
  },
  "stats_yesterday": {
    "amount": "0.00",
    "clicks": 0,
    "shows": 0
  },
  "status": "active",
  "system_status": "active",
  "telephone": "",
  "text": "Кот кататься не привык, опрокинул грузовик.",
  "title": "Accident",
  "updated": "2013-06-28 13:07:09",
  "url": "http://wikipedia.org/",
  "user": {
    "id": 1030027
  }
}
</code></pre>

### Изменение параметров объявления
`POST /api/v1/banners/{banner_id}.json`

<p>Метод изменяет параметры объявления, переданные в запросе в виде объекта
<a href="#object_banner">Banner</a>. В случае успешного изменения в ответе возвращается объект
<a href="#object_banner">Banner</a> с изменёнными параметрами.</p>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>POST /api/v1/banners/687419.json HTTP/1.1
Host: target-sandbox.mail.ru
Content-Type: application/json
Content-Length: 37
Accept-Encoding: gzip, deflate, compress
Authorization: AuthHMAC 9dEOYqb3sEmwKG9:ZmgUiT8huKqRkPhaSa/bZuuytAY=

{"title": "\u0442\u0435\u0441\u0442"}
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl \
-d '{"title": "\u0442\u0435\u0441\u0442"}' \
-H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:ZmgUiT8huKqRkPhaSa/bZuuytAY=' \
'https://target-sandbox.mail.ru/api/v1/banners/687419.json'
</code></pre>
<p>Пример ответа:</p>
<pre><code>{
  "moderation_reason_display": "",
  "moderation_status": "new",
  "status": "active",
  "system_status": "active",
  "title": "тест"
}
</code></pre>

### Получение списка всех объявлений кампании
`GET /api/v1/campaigns/{campaign_id}/banners.json`

<p>Метод позволяет получить список всех объявлений (объектов типа <a href="#object_banner">Banner</a>),
относящихся к указанной рекламной кампании, с возможностью
фильтрации по статусу.</p>
<p>Значение для фильтрации по статусу объявления задаётся GET-параметром
<code>status</code>. Возможные значения: <code>active</code>, <code>blocked</code>, <code>deleted</code>. Символ <code>-</code>
перед значением статуса инвертирует фильтр.</p>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>GET /api/v1/campaigns/334648/banners.json HTTP/1.1
Host: target-sandbox.mail.ru
Accept-Encoding: gzip, deflate, compress
Authorization: AuthHMAC 9dEOYqb3sEmwKG9:P36bjwx5Il9jxuc/ODx0UyKiV4Y=
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl \
-H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:P36bjwx5Il9jxuc/ODx0UyKiV4Y=' \
'https://target-sandbox.mail.ru/api/v1/campaigns/334648/banners.json'
</code></pre>
<p>Пример ответа:</p>
<pre><code>[
  {
    "banner_fields": [
      "title",
      "text",
      "url",
      "image"
    ],
    "banner_moderation": {
      "moderation_comment": "",
      "moderation_reason": ""
    },
    "campaign": {
      "id": 334648,
      "url": "/api/v1/campaigns/334648.json"
    },
    "company_name": "",
    "created": "2013-06-26 22:57:20",
    "edit_url": "/ads/banners/687418/edit/",
    "id": 687418,
    "image": {
      "height": 45,
      "id": 24512,
      "is_animated": false,
      "preview_url": "https://rb.mail.ru/img/36/6C4A7E.jpg",
      "size": 1607,
      "type": "static",
      "url": "http://r.mail.ru/img/36/6C4A7E.jpg",
    },
    "json_url": "/api/v1/banners/687418.json",
    "moderation_reason_display": "",
    "moderation_status": "allowed",
    "preview_image_url": "https://rb.mail.ru/img/36/6C4A7E.jpg",
    "status": "active",
    "system_status": "active",
    "telephone": "",
    "text": "Testov",
    "title": "Test",
    "updated": "2013-06-27 13:50:30",
    "url": "http://mail.ru/",
    "user": {
      "id": 1030027
    }
  },
  {
    "banner_fields": [
      "title",
      "text",
      "url",
      "image"
    ],
    "banner_moderation": {
      "moderation_comment": "",
      "moderation_reason": ""
    },
    "campaign": {
      "id": 334648,
      "url": "/api/v1/campaigns/334648.json"
    },
    "company_name": "",
    "created": "2013-06-27 13:50:09",
    "edit_url": "/ads/banners/687419/edit/",
    "id": 687419,
    "image": {
      "height": 45,
      "id": 24513,
      "is_animated": false,
      "preview_url": "https://rb.mail.ru/img/BA/573CCB.jpg",
      "size": 1616,
      "type": "static",
      "url": "http://r.mail.ru/img/BA/573CCB.jpg",
      "width": 60
    },
    "json_url": "/api/v1/banners/687419.json",
    "moderation_reason_display": "",
    "moderation_status": "new",
    "preview_image_url": "https://rb.mail.ru/img/BA/573CCB.jpg",
    "status": "active",
    "system_status": "active",
    "telephone": "",
    "text": "Кот кататься не привык, опрокинул грузовик.",
    "title": "тест",
    "updated": "2013-06-28 15:21:29",
    "url": "http://wikipedia.org/",
    "user": {
      "id": 1030027
    }
  }
]
</code></pre>

### Создание объявления
`POST /api/v1/campaigns/{campaign_id}/banners.json`

<p>Метод позволяет создать рекламное объявление с параметрами, переданными в
виде объекта <a href="#object_banner">Banner</a>. В случае успеха в ответе возвращается также объект
типа <a href="#object_banner">Banner</a> со всеми параметрами созданного объявления.</p>
<p>Кроме того, метод может принимать на вход список объектов <a href="#object_banner">Banner</a>.
Это позволяет создать несколько объявлений в кампании одним запросом.</p>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>POST /api/v1/campaigns/334648/banners.json HTTP/1.1
Host: target-sandbox.mail.ru
Content-Type: application/json
Content-Length: 671
Accept-Encoding: gzip, deflate, compress
Authorization: AuthHMAC 9dEOYqb3sEmwKG9:FnZwoO5Iin+Hwe8734HQ9f3LYSQ=

{"text":"тестовое объявление","title":"тест","preview_image_url":"https://rb.mail.ru/img/36/6C4A7E.jpg","edit_url":"","company_name":"","telephone":"","ctr_status":"good","moderation_status":"new","image":{"height":45,"width":60,"preview_url":"https://rb.mail.ru/img/36/6C4A7E.jpg","url":"http://r.mail.ru/img/36/6C4A7E.jpg","size":1607,"is_animated":false,"id":24512,"type":"static"},"url":"http://test.ru/","banner_moderation":{"moderation_comment":null,"moderation_reason":null},"stats":{"clicks":0,"shows":0},"stats_today":{"clicks":0,"shows":0},"stats_yesterday":{"clicks":0,"shows":0},"moderation_reason_display":null,"campaign":{"id":334648}}
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl \
-d '{"text":"тестовое объявление","title":"тест","preview_image_url":"https://rb.mail.ru/img/36/6C4A7E.jpg","edit_url":"","company_name":"","telephone":"","ctr_status":"good","moderation_status":"new","image":{"height":45,"width":60,"preview_url":"https://rb.mail.ru/img/36/6C4A7E.jpg","url":"http://r.mail.ru/img/36/6C4A7E.jpg","size":1607,"is_animated":false,"id":24512,"type":"static"},"url":"http://test.ru/","banner_moderation":{"moderation_comment":null,"moderation_reason":null},"stats":{"clicks":0,"shows":0},"stats_today":{"clicks":0,"shows":0},"stats_yesterday":{"clicks":0,"shows":0},"moderation_reason_display":null,"campaign":{"id":334648}}' \
-H 'Authorization: AuthHMAC 9dEOYqb3sEmwKG9:FnZwoO5Iin+Hwe8734HQ9f3LYSQ=' \
'https://target-sandbox.mail.ru/api/v1/campaigns/334648/banners.json'
</code></pre>
<p>Пример ответа:</p>
<pre><code>{
  "banner_fields": [
    "title",
    "text",
    "url",
    "image"
  ],
  "banner_moderation": {
    "moderation_comment": "",
    "moderation_reason": ""
  },
  "campaign": {
    "id": 334648,
    "url": "/api/v1/campaigns/334648.json"
  },
  "company_name": "",
  "created": "2013-06-29 17:58:03",
  "edit_url": "/ads/banners/687424/edit/",
  "id": 687424,
  "image": {
    "height": 45,
    "id": 24512,
    "is_animated": false,
    "preview_url": "https://rb.mail.ru/img/36/6C4A7E.jpg",
    "size": 1607,
    "type": "static",
    "url": "http://r.mail.ru/img/36/6C4A7E.jpg",
    "width": 60
  },
  "json_url": "/api/v1/banners/687424.json",
  "moderation_reason_display": "",
  "moderation_status": "new",
  "preview_image_url": "https://rb.mail.ru/img/36/6C4A7E.jpg",
  "status": "active",
  "system_status": "active",
  "telephone": "",
  "text": "тестовое объявление",
  "title": "тест",
  "updated": "2013-06-29 17:58:03",
  "url": "http://test.ru/",
  "user": {
    "id": 1030027
  }
}
</code></pre>

### Получение списка всех рекламных объявлений пользователя
`GET /api/v1/banners.json`

<p>Метод позволяет получить список всех объявлений (объектов типа
<a href="#object_bannerstat">BannerStat</a>), принадлежащих текущему пользователю, с возможностью
фильтрации по статусу как самих объявлений, так и кампаний, к которым они
относятся.</p>
<p>Значение для фильтрации по статусу объявления задаётся GET-параметром
<code>status</code>. Возможные значения: <code>active</code>, <code>blocked</code>, <code>deleted</code>. Символ <code>-</code>
перед значением статуса инвертирует фильтр.</p>
<p>Значение для фильтрации по статусу кампании, которой принадлежит
объявление, задаётся параметром <code>campaign__status</code>. Параметр имеет те же
допустимые значения и принимает символ <code>-</code> в начале.</p>

#### Пример

<p>HTTP-запрос:</p>
<pre><code>GET /api/v1/banners.json HTTP/1.1
Host: target-sandbox.mail.ru
Content-Type: application/json
Accept-Encoding: gzip, deflate, compress
Authorization: AuthHMAC Bv2BaJv95g68G39:Rv7DHZoSDfwHYgzAOBcaVwp54UI=
</code></pre>
<p>Curl-запрос:</p>
<pre><code>curl \
-H 'Authorization: AuthHMAC Bv2BaJv95g68G39:Rv7DHZoSDfwHYgzAOBcaVwp54UI=' \
'https://target-sandbox.mail.ru/api/v1/banners.json'
</code></pre>
<p>Пример ответа:</p>
<pre><code>[
  {
    "banner_fields": [
      "title",
      "text",
      "url",
      "image"
    ],
    "banner_moderation": {
      "moderation_comment": "Объявление не содержит осмысленного текста.",
      "moderation_reason": "CUSTOM"
    },
    "campaign": {
      "id": 268888,
      "url": "/api/v1/campaigns/268888.json"
    },
    "company_name": "",
    "created": "2011-09-08 17:23:43",
    "ctr_status": "good",
    "edit_url": "/ads/banners/529397/edit/",
    "id": 529397,
    "image": {
      "height": 31,
      "id": 6132,
      "is_animated": false,
      "preview_url": "https://rb.mail.ru/img/37/1FC5FA.png",
      "size": 3975,
      "type": "static",
      "url": "http://r.mail.ru/img/37/1FC5FA.png",
      "width": 60
    },
    "json_url": "/api/v1/banners/529397.json",
    "moderation_reason_display": "Объявление не содержит осмысленного текста.",
    "moderation_status": "banned",
    "preview_image_url": "https://rb.mail.ru/img/37/1FC5FA.png",
    "stats": {
      "amount": "0.00",
      "clicks": 0,
      "shows": 0
    },
    "stats_today": {
      "amount": "0.00",
      "clicks": 0,
      "shows": 0
    },
    "stats_yesterday": {
      "amount": "0.00",
      "clicks": 0,
      "shows": 0
    },
    "status": "deleted",
    "system_status": "active",
    "telephone": "",
    "text": "Test Kirillov. Test Kirillov",
    "title": "Test Kirillov",
    "updated": "2013-06-11 19:00:09",
    "url": "http://ya.ru/",
    "user": {
      "id": 1007846
    }
  }
]
</code></pre>
