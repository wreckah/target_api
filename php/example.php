<?php
require_once 'target_api_client.php';

use MailRu\TargetApi as Api;

$access_id = '9dEOYqb3sEmwKG9';
$private_key = 'u2bZIGvCJXxieTI';

$client = new Api\Client($access_id, $private_key);

$params = array('fields' => 'id,name,created,budget_limit');
$campaigns = $client->request('GET', 'campaigns.json', null, $params);
foreach ($campaigns as $campaign) {
    printf(
        "Campaign %s (#%d, created at %s) has budget limit %d\n",
        $campaign['name'],
        $campaign['id'],
        $campaign['created'],
        $campaign['budget_limit']
    );
}

$packages = $client->request('GET', 'packages.json');
foreach ($packages as $package) {
    if ($package['status'] === 'active') {
        break;
    }
}

$data = array(
    'name' => 'Test campaign',
    'package' => array('id' => $package['id']),
    'targetings' => array(
        'regions' => array(188),
        'sex' => 'MF',
        'age' => array(20, 21),
        'pads' => $package['targetings']['pads'],
    )
);
$new_campaign = $client->request('POST', 'campaigns.json', $data);
printf("New campaign has id: %d\n", $new_campaign['id']);

try {
    $client->request('POST', 'campaigns.json', array('name'=>'aaa'));
} catch (Api\Error $e) {
    print($e);
}

try {
    $client2 = new Api\Client('123', '456');
    $client2->request('GET', 'campaigns.json');
} catch (Api\Error $e) {
    print($e);
}

try {
    $client->request('GET', 'bad.json');
} catch (Api\Error $e) {
    print($e);
}
