# meagram

in Latin, "mea" means "my own" and in Greek "gram" means "things written"

run with uwsgi

    > uwsgi --http-socket <ip:port> --wsgi-file host.py

or 
    > uwsgi --http :<port> -w <file>:<obj>

configure nginx
```
    http {
    #other configuration
    
        server {
            location / {
                include uwsgi_params;
                uwsgi_pass <ip:port>;
            }
    }
```
