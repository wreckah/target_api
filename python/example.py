from target_api_client import Client

access_id = '9dEOYqb3sEmwKG9'
private_key = 'u2bZIGvCJXxieTI'

client = Client(access_id, private_key)

campaigns = client.request('campaigns.json', get_params={'fields': 'id,name,created,budget_limit'})
for campaign in campaigns:
    print(
        'Campaign %(name)s (#%(id)d, created at %(created)s)' +
        ' has budget limit %(budget_limit)s' % campaign
    )

packages = client.request('packages.json')
for package in packages:
    if package['status'] == 'active':
        break

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
print('New campaign has id: %d', new_campaign['id'])

# try {
#     $client->request('POST', 'campaigns.json', array('name'=>'aaa'));
# } catch (Api\Error $e) {
#     print($e);
# }
# 
# try {
#     $client2 = new Api\Client('123', '456');
#     $client2->request('GET', 'campaigns.json');
# } catch (Api\Error $e) {
#     print($e);
# }
# 
# try {
#     $client->request('GET', 'bad.json');
# } catch (Api\Error $e) {
#     print($e);
# }
