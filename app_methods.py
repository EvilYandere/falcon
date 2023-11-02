import json
import falcon


class ObjectRequest:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

        data = json.loads(req.stream. read())

        output = {
            'msg': 'Hey {0}'.format(data['name'])
        }

        resp.body = json.dumps(output)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200

        data = json.loads(req. stream. read())
        eq = int(data['x']) + int(data['y'])

        output = {
            'msg': 'x: {x} + y: {y} is {e}'.format(x=data['x'], y=data['y'], e=eq)
        }
        resp.body = json.dumps(output)


    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200

        output = {
            'msg': 'Will be later...maybe'
        }

        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/methods', ObjectRequest())

# waitress-serve --listen=*:8001 app_methods:api
