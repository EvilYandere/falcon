import json
import falcon


class ObjectRequest:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

        validate_params = True

        if 'username' not in req.params:
            validate_params = False

        if 'id' not in req.params:
            validate_params = False

        if validate_params is True:
            output = {
                'username': req.params['username'],
                'id': req.params['id']
            }
        else:
            output = {
                'error': 'ID needed'
            }

        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/validate_params', ObjectRequest())

# waitress-serve --listen=*:8001 app_validate_params:api
