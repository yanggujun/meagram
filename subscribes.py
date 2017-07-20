import falcon
import json

class SubscribesController(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        subs = [{'name': 'programming'}, {'name': 'soccer'}, {'name': 'csharp'}]
        resp.body = json.dumps(subs)
