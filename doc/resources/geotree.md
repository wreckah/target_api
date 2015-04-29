## География


### Получение гео-дерева
`GET /api/v1/geo_tree.json`

Метод позволяет получить страны и регионы в виде дерева.

#### Пример

HTTP-запрос:

    GET /api/v1/geo_tree.json HTTP/1.1
    Host: target-sandbox.my.com
    Accept-Encoding: gzip, deflate, compress
    Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18

Curl-запрос:

    curl \
    -H 'Authorization: Bearer Bh8kQmBUwgGDLuprqZhfMMm..7JrLbTAEFbEv74TydrC18' \
    'https://target-sandbox.my.com/api/v1/geo_tree.json'

Пример ответа:

    [
      {
        "children": [
          {
            "id": 7,
            "level": 2,
            "name": "Алтайский край",
            "share": 45988143,
            "type": "city",
            "user_geo_cnt": 64,
            "user_geo_ready": true
          },
          {
            "id": 10,
            "level": 2,
            "name": "Амурская область",
            "share": 9481304,
            "type": "city",
            "user_geo_cnt": 26,
            "user_geo_ready": true
          },
          ...
        ],
        "id": 188,
        "level": 1,
        "name": "Россия",
        "share": 2302119771,
        "type": "city",
        "user_geo_cnt": 0,
        "user_geo_ready": false
      },
      {
        "children": [
          {
            "id": 219,
            "level": 2,
            "name": "Азербайджан",
            "share": 21180714,
            "type": "city",
            "user_geo_cnt": 11,
            "user_geo_ready": true
          },
          {
            "id": 215,
            "level": 2,
            "name": "Армения",
            "share": 50084719,
            "type": "city",
            "user_geo_cnt": 18,
            "user_geo_ready": true
          },
          {
            "children": [
              {
                "id": 286,
                "level": 3,
                "name": "Брестская область",
                "share": 7097659,
                "type": "city",
                "user_geo_cnt": 16,
                "user_geo_ready": true
              },
              {
                "id": 287,
                "level": 3,
                "name": "Витебская область",
                "share": 7270598,
                "type": "city",
                "user_geo_cnt": 19,
                "user_geo_ready": true
              },
              ...
            ],
            "id": 201,
            "level": 2,
            "name": "Беларусь",
            "share": 89234923,
            "type": "city",
            "user_geo_cnt": 0,
            "user_geo_ready": false
          },
          ...
        ],
        "id": 100001,
        "level": 1,
        "name": "Бывший СССР",
        "share": 763254134,
        "type": "abstract",
        "user_geo_cnt": 0,
        "user_geo_ready": false
      },
      {
        "children": [
          {
            "id": 218,
            "level": 2,
            "name": "Австрия",
            "share": 662174,
            "type": "city",
            "user_geo_cnt": 0,
            "user_geo_ready": false
          },
          {
            "id": 206,
            "level": 2,
            "name": "Албания",
            "share": 27916,
            "type": "city",
            "user_geo_cnt": 0,
            "user_geo_ready": false
          },
          ...
        ],
        "id": 100002,
        "level": 1,
        "name": "Европа",
        "share": 104756947,
        "type": "abstract",
        "user_geo_cnt": 0,
        "user_geo_ready": false
      },
      {
        "children": [
          {
            "id": 204,
            "level": 2,
            "name": "Афганистан",
            "share": 12034,
            "type": "city",
            "user_geo_cnt": 0,
            "user_geo_ready": false
          },
          {
            "id": 222,
            "level": 2,
            "name": "Бангладеш",
            "share": 4098,
            "type": "city",
            "user_geo_cnt": 0,
            "user_geo_ready": false
          },
          ...
        ],
        "id": 100003,
        "level": 1,
        "name": "Азия",
        "share": 19245976,
        "type": "abstract",
        "user_geo_cnt": 0,
        "user_geo_ready": false
      },
      {
        "children": [
          {
            "id": 220,
            "level": 2,
            "name": "Багамы",
            "share": 608,
            "type": "city",
            "user_geo_cnt": 0,
            "user_geo_ready": false
          },
          {
            "id": 116,
            "level": 2,
            "name": "Гаити",
            "share": 188,
            "type": "city",
            "user_geo_cnt": 0,
            "user_geo_ready": false
          },
          ...
        ],
        "id": 100005,
        "level": 1,
        "name": "Северная Америка",
        "share": 6528881,
        "type": "abstract",
        "user_geo_cnt": 0,
        "user_geo_ready": false
      },
      {
        "children": [
          {
            "children": [
              {
                "id": 217,
                "level": 3,
                "name": "Австралия",
                "share": 173093,
                "type": "city",
                "user_geo_cnt": 0,
                "user_geo_ready": false
              },
              {
                "id": 410,
                "level": 3,
                "name": "Вануату",
                "share": 24,
                "type": "city",
                "user_geo_cnt": 0,
                "user_geo_ready": false
              },
              ...
            ],
            "id": 100007,
            "level": 2,
            "name": "Австралия и Океания",
            "share": 238076,
            "type": "abstract",
            "user_geo_cnt": 0,
            "user_geo_ready": false
          },
          {
            "children": [
              {
                "id": 413,
                "level": 3,
                "name": "Антарктика",
                "share": 394,
                "type": "city",
                "user_geo_cnt": 0,
                "user_geo_ready": false
              }
            ],
            "id": 100008,
            "level": 2,
            "name": "Антарктика",
            "share": 394,
            "type": "abstract",
            "user_geo_cnt": 0,
            "user_geo_ready": false
          },
          {
            "children": [
              {
                "id": 207,
                "level": 3,
                "name": "Алжир",
                "share": 23160,
                "type": "city",
                "user_geo_cnt": 0,
                "user_geo_ready": false
              },
              {
                "id": 210,
                "level": 3,
                "name": "Ангола",
                "share": 6464,
                "type": "city",
                "user_geo_cnt": 0,
                "user_geo_ready": false
              },
              ...
            ],
            "id": 100004,
            "level": 2,
            "name": "Африка",
            "share": 422888,
            "type": "abstract",
            "user_geo_cnt": 0,
            "user_geo_ready": false
          },
          {
            "children": [
              {
                "id": 214,
                "level": 3,
                "name": "Аргентина",
                "share": 102987,
                "type": "city",
                "user_geo_cnt": 0,
                "user_geo_ready": false
              },
              {
                "id": 226,
                "level": 3,
                "name": "Белиз",
                "share": 48,
                "type": "city",
                "user_geo_cnt": 0,
                "user_geo_ready": false
              },
              ...
            ],
            "id": 100006,
            "level": 2,
            "name": "Латинская Америка",
            "share": 223213,
            "type": "abstract",
            "user_geo_cnt": 0,
            "user_geo_ready": false
          }
        ],
        "id": 100009,
        "level": 1,
        "name": "Остальной мир",
        "share": 884571,
        "type": "abstract",
        "user_geo_cnt": 0,
        "user_geo_ready": false
      }
    ]

