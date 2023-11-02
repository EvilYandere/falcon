import json
import falcon


class ObjectRequest:
    __json_content = {}

    def __validate_json(self, req):
        try:
            self.__json_content = json.loads(req.stream.read())
            print("json validated")
            return True

        except ValueError as e:
            self.__json_content = {}
            print("json NOT validated ", e)
            return False

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        validated = self.__validate_json(req)

        output = {
            'status': 200,
            'message': None
        }

        if validated:
            if "name" in self.__json_content:

                output = {
                    'msg': 'Hey {0}'.format(self.__json_content['name'])
                }

            else:
                output['status'] = 404
                output['message'] = 'param "name" required'
        else:
            output['status'] = 404
            output['message'] = 'validation failed'

        resp.body = json.dumps(output)


api = falcon.API()
api.add_route('/validate_json', ObjectRequest())

# waitress-serve --listen=*:8001 app_validate_json:api
