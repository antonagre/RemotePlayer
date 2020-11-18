import player
from Pyro5.api import expose, Daemon, locate_ns

@expose
class PyroBridge():
    def __init__(self):
        self.player=player.getPlayer()

    def play(self,name):
        self.player.play(name)

    @expose
    def next(self):
        self.next()

    @expose
    def prev(self):
        self.player.prev()

    @expose
    def pause(self):
        self.player.pause()


    @expose
    def resume(self):
        self.player.resume()


    @expose
    def stop(self):
        self.player.stop()


def run():
    daemon = Daemon()  # make a Pyro daemon
    ns = locate_ns("127.0.0.1")# find the name server
    uri = daemon.register(PyroBridge)   # register the greeting maker as a Pyro object
    print("Ready. Object uri = "+str(uri))      # log( the uri so we can use it in the client later
    ns.register("player-rmi", uri)
    print("Pyro Server Loaded and Running")
    daemon.requestLoop()


run()