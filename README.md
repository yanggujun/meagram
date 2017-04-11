# meagram

in Latin, "mea" means "my own" and in Greek "gram" means "things written"

run with uwsgi

    > uswgi --http-socket <ip:port> --wsgi-file host.py

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
