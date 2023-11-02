import falcon
import base64

user_accounts = {
    'someuser': 'pass'
}


class Authorize(object):
    def __init__(self):
        pass

    def __auth_basic(self, username, password):
        if username in user_accounts and user_accounts[username] == password:
            print('Your have access. Welcome,', username)
        else:
            raise falcon.HTTPUnauthorized('Unauthorized', 'Your access is not allowed')

    def __call__(self, req, resp, resource, params):
        print('before trigger - class: Authorize')
        auth_exp = req.auth.split(' ') if req.auth is not None else (None, None,)

        if auth_exp[0] is None or auth_exp[0].lower() != "basic":
            raise falcon.HTTPNotImplemented('Not Implement', 'You don\'t use the right auth method')

        else:
            auth = base64.b64decode(auth_exp[1]).decode('utf-8').split(':')
            username = auth[0]
            password = auth[1]
            self.__auth_basic(username, password)


class ObjectResource:
    @falcon.before(Authorize())
    def on_get(self, req, resp):
        print('on_get trigger')

        output = {
            'method': 'get',
            'message': 'Welcome'
        }
        resp.media = output


api = falcon.API()
api.add_route('/auth', ObjectResource())

# waitress-serve --listen=*:8001 app_auth:api
