import falcon
import json


class ObjectRequest:
    def on_get(self, req, resp):
        content = {
            'username' : 'test',
            'id' : '1337'
        }

        resp.body = json.dumps(content)


api = falcon.API()
api.add_route('/', ObjectRequest())

# waitress-serve --listen=*:8001 app_main:api
