## Using

### Initializing API client
```python
import target_api_client

client_id = 'Yu1ES2t2VuPBYQ2f'
client_secret = '8rhRaKLEnv*****IdqmkaiQkqO8HUYL2TObVB'

client = target_api_client.TargetApiClient(client_id, client_secret)
```

### Obtaining an access token
This is an access token obtained by `Client Credentials Grant` flow of OAuth2.
```python
access_token = client.request_client_token()
print(access_token)
token = access_token['access_token']
```

Use `access_token` property from the response as a value for `Authorization`
HTTP header for all requests:
```
GET /api/v1/campaigns.json HTTP/1.1
Host: target.my.com
Authorization: Bearer FvlLLzFv4u5DPK...MEGrUnnpFyZTMkLKmHOIbfO0ML1tfmCtyOVH
```

### Refreshing an expired access token
```python
try:
    # Doing something with API.
    pass
except target_api_client.TargetAuthError as e:
    if e.message == 'Access token is expired':
        access_token = client.refresh_access_token(
            access_token['refresh_token']
        )
    else:
        raise e
```

### Getting campaigns

```python
campaigns = client.request(
    'campaigns.json', token, params={'fields': 'id,name,created,budget_limit'}
)
print(campaigns)
```

### Getting all packages and selecting a particular one
Getting packages:
```python
packages = client.request('packages.json', token)
for package in packages:
    if package['name'] == 'multiple_external_90_75':
        break
print(package)
```

### Creating a campaign with selected package
```python
data = {
    'name': 'Test campaign',
    'package': {'id': package['id']},
    'targetings': {
        'regions': [188],
        'sex': 'MF',
        'age': [20, 21],
        'pads': package['targetings']['pads'],
    }
}
campaign = client.request('campaigns.json', token, data=data)
print(campaign)
```

### Uploading an image
```python
import requests

image_url = 'https://raw.githubusercontent.com/wreckah/target_api/master/image.jpg'
image = client.request('images.json', token, files={
    'banner_format_id': ('', str(package['banner_format']['id']), 'form-data'),
    'image_file': ('image.jpg', requests.get(image_url).content, 'image/jpeg'),
})
print(image)
```

### Creating a banner
```python
data = {
    'image': {'id': image['id']},
    'text': 'test message',
    'title': 'test banner',
    'url': 'http://www.w3c.org/',
}
banner = client.request(
    'campaigns/%s/banners.json' % campaign['id'], token, data
)
print(banner)
```

## Handling errors

### Validation error
HTTP status code is 400.
```python
try:
    client.request('campaigns.json', token, data={'name': 'aaa'})
except target_api_client.TargetValidationError as e:
    print(e)
    print(e.fields)
```

### Authentication error
HTTP status code is 401.
```python
try:
    client.request('campaigns.json', 'bad_access_token')
except TargetAuthError as e:
    print(e)
    print(e.oauth_message)
```

### Other errors
```python
try:
    client.request('bad.json', token)
except TargetApiError as e:
    # NotFound error
    print(e)
```
