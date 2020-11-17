#!/usr/bin/python3
import pexpect
import json


########NODE CLIENT HELPER########################
p = pexpect.spawn("mpsyt")
playing = False

def execCommand(command):
    command=command.lower()
    returnCode=processCommand(command)
    if(not returnCode):
        print("command not valid, try again")

def processCommand(message):
    global playing
    if(message.find(".")>0):
        data=message.split(".")
        command=data[0]
    else:
        command=message
    try:
        args=str(data[1])
    except:
        args=None
    print("command: "+command+" args:"+str(args))
    if(command=="play"):
        if(playing):
            stop()
        p.sendline('/'+args)
        p.sendline("1")
        print("PLAYING")
        playing=True
    elif(command=="next"):
        p.sendline('>')
    elif(command=="stop"):
        stop()
    elif(command=="resume"):
        resume()
    elif(command=="pause"):
        pause()
    elif(command=="previous"):
        p.sendline('<')
    else:
        return False
    return True

def stop():
    global playing
    print("STOP")
    p.sendcontrol("c")
    playing=False

def pause():
    global playing
    p.send(" ")
    playing=False

def resume():
    global playing
    p.send(" ")
    playing=True




