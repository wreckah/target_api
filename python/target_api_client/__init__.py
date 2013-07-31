from binascii import b2a_base64
from hashlib import sha1
from hmac import new
from json import dumps, loads
try:
    # For Python 3.0 and later.
    from urllib.parse import quote, urlencode
    from urllib.request import HTTPError, Request, urlopen
except ImportError:
    # Fall back to Python 2's urllib2.
    from urllib2 import HTTPError, Request, urlopen
    from urllib import quote, urlencode


class TargetApiError(Exception):
    def __init__(self, message, code=500, fields=None):
        self.message = message
        self.code = code
        if fields:
            self.fields = fields

    def __str__(self):
        if self.code == 400:
            return 'TargetApiError %s: %s\n  %s' % (
                self.code,
                self.message,
                '\n  '.join(
                    '#%s: %s' % (f, e) for f, e in self.fields.items()
                )
            )
        else:
            return 'TargetApiError %s: %s' % (self.code, self.message)


class TargetApiClient(object):
    HTTP_METHODS = {'GET', 'POST', 'DELETE'}
    PRODUCTION_HOST = 'target.mail.ru'
    SANDBOX_HOST = 'target-sandbox.mail.ru'
    access_id = None
    private_key = None
    url = None

    def __init__(self, access_id, private_key, is_sandbox=True, version=1):
        self.access_id = access_id
        self.private_key = private_key.encode()
        host = self.SANDBOX_HOST if is_sandbox else self.PRODUCTION_HOST
        self.url = 'https://%s/api/v%d/' % (host, version)

    def request(self, resource, method='GET', post_data=None, get_params=None):
        method = method.upper()
        assert method in self.HTTP_METHODS, \
            'Unsupported HTTP method: %s. Supported methods are: %s' % (
                method,
                ', '.join(self.HTTP_METHODS)
            )

        # Prepare authentication signature.
        data = dumps(post_data) if post_data else ''
        url = self.url + resource.lstrip('/')
        string = '%s&%s&%s' % (
            method,
            quote(url, safe='~'),
            quote(data, safe='~')
        )
        signature = b2a_base64(
            new(self.private_key, string.encode(), sha1).digest()
        ).decode().rstrip('\n')

        # Perform HTTP request.
        if get_params:
            url += '?' + urlencode(get_params)
        req = Request(url, data.encode() if data else None)
        req.add_header(
            'Authorization',
            'AuthHMAC %s:%s' % (self.access_id, signature)
        )
        if data:
            req.add_header('Content-Type', 'application/json')
        try:
            return loads(urlopen(req).read().decode())
        except HTTPError as e:
            message = loads(e.read().decode())
            if e.code == 400:
                raise TargetApiError(
                    'ValidationError',
                    code=400,
                    fields=message
                )
            raise TargetApiError(message, e.code)
