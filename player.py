#!/usr/bin/python3
import pexpect
import alsaaudio
playing = False

__instance__ = None


def getPlayer():
    global __instance__
    if(__instance__==None):
        __instance__= Player()
    return __instance__

class Player():

    def __init__(self):
        self.p = pexpect.spawn("mpsyt")
        try:
            self.mixer = alsaaudio.Mixer('Headphone')
        except:
            self.mixer = alsaaudio.Mixer()

    def play(self,name):
        global playing
        if(playing):
            self.stop()
        self.p.sendline('/'+name)
        self.p.sendline("1")
        print("PLAYING")
        playing=True

    def next(self):
        self.p.sendline('>')

    def previous(self):
        self.p.sendline('<')

    def volUp(self):
        v=self.mixer.getvolume()[0]+10
        print(v)
        if(v<=100):
            self.mixer.setvolume(v)
    def volDown(self):
        v=self.mixer.getvolume()[0]-10
        print(v)
        if(v>=0):
            self.mixer.setvolume(v)

    def setVol(self,v):
        if(v<=100):
            self.mixer.setvolume(v)

    def stop(self):
        global playing
        print("STOP")
        self.p.sendcontrol("c")
        playing=False

    def pause(self):
        global playing
        self.p.send(" ")
        playing=False

    def resume(self):
        global playing
        self.p.send(" ")
        playing=True