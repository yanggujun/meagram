from host import Host
from login import LoginController
from subscribes import SubscribesController

login = LoginController()
subs = SubscribesController()

host = Host();
host.add_route('/login', login)
host.add_route('/subscribes', subs)
