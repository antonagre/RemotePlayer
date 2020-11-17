#!/usr/bin/python3
import paho.mqtt.client as mqtt
import player
import config

broker_address= config.broker_address  #Broker address
port = config.mqttPort                         #Broker port
user = config.mqttUser                    #Connection username
password = config.mqttPassword            #Connection password
topic = config.deviceName+'/player'

def on_message(client, userdata, message):
    print(0)
    text=message.payload.decode("utf-8")
    print("message received " ,text)
    player.execCommand(text)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)
    print("Subscribing to topic",topic)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message=on_message        #attach function to callback
client.username_pw_set(user,password) ## set mqtt username and password
client.connect(broker_address,port,60)

##start pooling loop
client.loop_forever()
