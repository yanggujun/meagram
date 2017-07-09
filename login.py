import falcon
import json

class LoginController:
    def on_post(self, req, resp):
        body = req.stream.read()
        loginInfo = json.loads(body)
        print 'user: ' + loginInfo['userName']
        print 'pass: ' + loginInfo['password']
        resp.status = falcon.HTTP_200
        resp.body = 'ok'

