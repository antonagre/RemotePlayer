from youtube_search import YoutubeSearch
from mpv import MPV
import pafy
import json

mpv=MPV()
pos=0
songName=None

def getAudioUrl(searchString):
    print("Search: "+searchString)
    res = YoutubeSearch(searchString , max_results=10).to_json()
    data = json.loads(res)
    videoUrl="http://youtube.com"+data["videos"][0]["url_suffix"]
    video = pafy.new(videoUrl)
    return video.audiostreams[0].url

@mpv.property_observer('time-pos')
def time_observer(_name, value):
    global pos
    pos=value

def play(name):
    global songName
    url=getAudioUrl(name)
    songName=name
    mpv.play(url)

def pause():
    mpv.pause=True

def resume():
    mpv.pause=False

def seek(pos):
    x=pos-getCurPos()
    mpv.seek(x)

def getCurPos():
    global songName
    if(pos==None):
        songName = None
    return pos

def getInfo():
    data={}
    data["name"]=songName
    data["duration"]=mpv.duration
    data["pos"]=getCurPos()
    return json.dumps(data)