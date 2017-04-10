def application(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])

    path = env["PATH_INFO"]
    root = "./www"
    indexPage = "/index.html"
    fp = root
    if (path == "/"):
        fp = root + indexPage
    else:
        fp = root + path
    hf = open(fp, 'r')
    html = hf.read()
    hf.close()
    return html
