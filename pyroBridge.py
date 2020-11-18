from threading import Thread
from player import Player
from Pyro5.api import expose, Daemon, locate_ns

@expose
class PyroBridge(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.player=Player()
        Thread.daemon = True
        self.daemon = Daemon("192.168.1.202")  # make a Pyro daemon
        self.ns = locate_ns()# find the name server
        self.uri = self.daemon.register(self)   # register the greeting maker as a Pyro object
        print("Ready. Object uri = "+str(self.uri))      # log( the uri so we can use it in the client later
        self.ns.register("player-rmi", self.uri)
        print("Pyro Server Loaded and Running")

    def run(self):
        while(True):
            try:
                self.daemon.requestLoop()
            except:
                pass

    @expose
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


brg=PyroBridge()
brg.start()