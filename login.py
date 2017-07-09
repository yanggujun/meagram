import falcon

class LoginController:
    def on_get(self, req, resp):
        print 'I am logining!'
        resp.status = falcon.HTTP_200
        resp.body = 'ok'

