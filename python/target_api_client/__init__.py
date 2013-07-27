from binascii import b2a_base64
from hashlib import sha1
from hmac import new
from json import dumps, loads
from urllib import quote, urlencode
try:
    # For Python 3.0 and later.
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2.
    from urllib2 import HTTPError, Request, urlopen


class Error(Exception):
    def __init__(self, message, fields=None):
        super(Error, self).__init__(message)
        if fields:
            self.fields = fields

    def __unicode__(self):
        return super(Error, self).__unicode__()
#     {
#         $res = sprintf(
#             "Target API error: %s (#%d)\n",
#             $this->getMessage(),
#             $this->getCode()
#         );
#         if ($this->fields) {
#             foreach ($this->fields as $field => $error) {
#                 $res .= sprintf("  #%s: %s\n", $field, $error);
#             }
#         }
#         return $res . $this->getTraceAsString() .
#             sprintf("\n  thrown in %s on line %d\n", $this->getFile(), $this->getLine());
#     }


class Client(object):
    HTTP_METHODS = {'GET', 'POST', 'DELETE'}
    PRODUCTION_HOST = 'target.mail.ru'
    SANDBOX_HOST = 'target-sandbox.mail.ru'
    access_id = None
    private_key = None
    url = None

    def __init__(self, access_id, private_key, is_sandbox=True, version=1):
        self.access_id = access_id
        self.private_key = private_key
        host = self.SANDBOX_HOST if is_sandbox else self.PRODUCTION_HOST
        self.url = 'https://%s/api/v%d/' % (host, version)

    def request(self, resource, method='GET', post_data=None, get_params=None):
        method = method.upper()
        assert method in self.HTTP_METHODS, \
            'Unsupported HTTP method: %s. Supported methods are: %s' % (
                method,
                ', '.join(self.HTTP_METHODS)
            )
        data = dumps(post_data) if post_data else ''
        url = self.url + resource.lstrip('/')
        string = '%s&%s&%s' % (
            method,
            quote(url, safe='~'),
            quote(data, safe='~')
        )
        signature = b2a_base64(
            new(self.private_key, string, sha1).digest()
        ).rstrip('\n')

        if get_params:
            url += '?' + urlencode(get_params)
        req = Request(url, data or None)
        req.add_header(
            'Authorization',
            'AuthHMAC %s:%s' % (self.access_id, signature)
        )
        if data:
            req.add_header('Content-Type', 'application/json')
        try:
            res = urlopen(req).read()
        except HTTPError:
            raise
        return loads(res)
# 
#         $code = null;
#         if (isset($meta['wrapper_data']) && sizeof($meta['wrapper_data'])) {
#             $tmp = explode(' ', $meta['wrapper_data'][0]);
#             $code = sizeof($tmp) > 1 ? intval($tmp[1]) : null;
#         }
#         if ($code === 200) {
#             return $resp;
#         }
#         if ($code === 400) {
#             throw new Error('Validation failed', 400, null, $resp);
#         }
#         throw new Error($resp, $code);
#     }
# }
