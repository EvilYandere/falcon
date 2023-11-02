import json
import falcon


class ObjectRequest:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

        data = json.loads(req.stream.read())

        content = {
            'username': 'test',
            'id': '1337'
        }

        output = {}

        if 'method' not in data:
            resp.status = falcon.HTTP_501
        else:
            if data['method'] == 'get-username':
                output['value'] = content['username']
            else:
                resp.status = falcon.HTTP_404
                output['value'] = None

            resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/codes', ObjectRequest())

# waitress-serve --listen=*:8001 app_codes:api
