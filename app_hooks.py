import falcon


class Authorize(object):
    def __init__(self, roles):
        self._roles = roles

    def __call__(self, req, resp, resource, params):
        if 'Admin' in self._roles:
            resp.user_id = 1337

        else:
            raise falcon.HTTPBadRequest('Bad request', 'Admin rights needed')


class ObjectResource:
    @falcon.before(Authorize(['Admin', 'Normal', 'Guest']))
    def on_get(self, req, resp):
        print('trigger - get')

        output = {
            'method': 'get',
            'user_id': resp.user_id
        }
        resp.media = output

    def on_post(self, req, resp):
        print('trigger — post')

        output = {
            'method': 'get',
            'user_id': resp.user_id
        }
        resp.media = output


api = falcon.API()
api.add_route('/hooks', ObjectResource())

# waitress-serve --listen=*:8001 app_hooks:api
