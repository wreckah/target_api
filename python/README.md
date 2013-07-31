## Using

Initializing client:
```python
from target_api_client import TargetApiClient, TargetApiError

access_id = '9dEOYqb3sEmwKG9'
private_key = 'u2bZIGvCJXxieTI'

client = TargetApiClient(access_id, private_key)
```

Getting campaigns:
```python
campaigns = client.request('campaigns.json', get_params={'fields': 'id,name,created,budget_limit'})
for campaign in campaigns:
    print((
        'Campaign %(name)s (#%(id)d, created at %(created)s)' +
        ' has budget limit %(budget_limit)s'
    ) % campaign)
```

Getting packages:
```python
packages = client.request('packages.json')
for package in packages:
    if package['status'] == 'active':
        break
```

Creating campaign:
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
new_campaign = client.request('campaigns.json', 'POST', post_data=data)
print('New campaign has id: %d' % new_campaign['id'])
```

## Handling errors

Validation error (HTTP 400 code):
```python
try:
    client.request('campaigns.json', 'POST', {'name': 'aaa'})
except TargetApiError as e:
    print(e)
    print(e.fields)
```

Authentication error (HTTP 401 code):
```python
try:
    client2 = TargetApiClient('123', '456')
    client2.request('campaigns.json')
except TargetApiError as e:
    print(e)
```

Not found error (HTTP 404 code):
```python
try:
    client.request('bad.json')
except TargetApiError as e:
    print(e)
```
