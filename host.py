import os.path
import uuid
import json
import falcon

class Host:
    def __init__(self):
        self.id = uuid.uuid1()
        self.api = falcon.API()

    def __call__(self, env, start_response):
        response = "200 OK"
        mime = "text/html"
        # start_response("200 OK", [("Content-Type", "text/html")])


        path = env["PATH_INFO"]
        method = env["REQUEST_METHOD"]
         
        root = "./www"
        indexPage = "/index.html"
        fp = root
        if (path == "/"):
            fp = root + indexPage
        else:
            fp = root + path

        fileFound = os.path.exists(fp)

        if (fileFound == True):
            fn, ext = os.path.splitext(fp)
            if (ext == ".js"):
               mime = "application/javascript"
            elif (ext == ".css"):
                mime = "text/css"
            elif (ext == ".xml"):
                mime = "application/xml"
            elif (ext == ".png"):
                mime = "image/png"
            elif (ext == ".jpeg"):
                mime = "image/jpeg"
            elif (ext == ".gif"):
                mime = "image/gif"
            elif (ext == ".json"):
                mime = "application/json"

        html = ""
        if (fileFound == True):
            hf = open(fp, 'r')
            html = hf.read()
            hf.close()
        
        start_response(response, [("Content-Type", mime)])

        return html

    def add_route(self, uri_template, handler):
        api.add_route(uri_template, handler)

server = Host()
