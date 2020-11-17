#!/usr/bin/python3
import pexpect
import json


########NODE CLIENT HELPER########################
p = pexpect.spawn("mpsyt")
playing = False

def validate_message(command):
    command=command.lower()
    returnCode=processCommand(command)
    if(not returnCode):
        print("command not valid, try again")

def processCommand(message):
    global playing
    data=message.split(".")
    command=data[0]
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
###FUNCTION OF CLIENT NODE########################
def stop():
    global playing
    print("STOP")
    p.sendcontrol("c")
    playing=False

def ping_test():
    pass

def shutdown():
    args=json.loads(dat)
    subprocess.Popen("systemctl poweroff -i", shell=True)

def run_command(dat):
    args=json.loads(dat)
    command = helpers.append_helper([],args["command"])
    subprocess.Popen(command, shell=False)

def close_app(dat):
    args=json.loads(dat)
    command = helpers.append_helper(["killall"],args["command"])
    subprocess.Popen(command, shell=False)

def open_in_browser(dat):
    args=json.loads(dat)
    subprocess.Popen(["xdg-open", "http://" + args["url"]], shell=False)

def search_for(dat):
    args=json.loads(dat)
    query = settings.search_query.format(urlopen.quote(args["query"]))
    subprocess.Popen(["xdg-open", query], stdout=Core.FNULL, shell=False)

def pause():
    global playing
    p.send(" ")
    playing=False

def resume():
    global playing
    p.send(" ")
    playing=True




