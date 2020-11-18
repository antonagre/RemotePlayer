import Pyro5.api

nameserver = Pyro5.api.locate_ns("192.168.1.202")
uri = nameserver.lookup("player-rmi")
rmi = Pyro5.api.Proxy(uri)
rmi.play("bocca di rosa")