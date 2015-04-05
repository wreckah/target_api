import requests
from pprint import pprint
from target_api_client import (
    TargetApiClient, TargetApiError, TargetAuthError, TargetValidationError
)

client_id = 'Yu1ES2t2VuPBYQ2f'
client_secret = '8rhRaKLEnv*****IdqmkaiQkqO8HUYL2TObVB'

client = TargetApiClient(client_id, client_secret)

# Obtain an access token:
access_token = client.request_client_token()
token = access_token['access_token']
print('Access token:')
pprint(access_token)
print('-' * 80)

# Refresh the access token:
try:
    # Doing something with API.
    pass
except TargetAuthError as e:
    if e.message == 'Access token is expired':
        access_token = client.refresh_access_token(
            access_token['refresh_token']
        )
    else:
        raise e

# Get campaigns:
campaigns = client.request(
    'campaigns.json', token, params={'fields': 'id,name,created,budget_limit'}
)
print('Campaigns:')
pprint(campaigns)
print('-' * 80)

# Get packages and choose a particular one:
packages = client.request('packages.json', token)
for package in packages:
    if package['name'] == 'multiple_external_90_75':
        break
print('Package:')
pprint(package)
print('-' * 80)

# Create a campaign:
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
print('New campaign:')
pprint(campaign)
print('-' * 80)

# Upload an image:
image_url = 'https://raw.githubusercontent.com/wreckah/target_api/master/image.jpg'
image = client.request('images.json', token, files={
    'banner_format_id': ('', str(package['banner_format']['id']), 'form-data'),
    'image_file': ('image.jpg', requests.get(image_url).content, 'image/jpeg'),
})
print('Uploaded image')
pprint(image)
print('-' * 80)

# Create a banner:
data = {
    'image': {'id': image['id']},
    'text': 'test message',
    'title': 'test banner',
    'url': 'http://www.w3c.org/',
}
banner = client.request(
    'campaigns/%s/banners.json' % campaign['id'], token, data
)
print('New banner')
pprint(banner)
print('-' * 80)

# Catch validation error:
try:
    client.request('campaigns.json', token, data={'name': 'aaa'})
except TargetValidationError as e:
    print('Validation error')
    print(e)
    pprint(e.fields)
    print('-' * 80)

# Catch authentication error:
try:
    client.request('campaigns.json', 'bad_access_token')
except TargetAuthError as e:
    print('Auth error')
    print(e)
    print(e.oauth_message)
    print('-' * 80)

# Catch not found error:
try:
    client.request('bad.json', token)
except TargetApiError as e:
    print('Not found error')
    print(e)
    print('-' * 80)
