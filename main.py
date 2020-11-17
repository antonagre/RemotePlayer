#!/usr/bin/python3
import paho.mqtt.client as mqtt
import time 
import player
import config

broker_address= config.broker_address  #Broker address
port = config.mqttPort                         #Broker port
user = config.mqttUser                    #Connection username
password = config.mqttPassword            #Connection password
topic = config.deviceName+'/player'

def on_message(client, userdata, message):
    text=message.payload.decode("utf-8")
    print("message received " ,text)
    player.execCommand(text)

def on_connect(client, userdata, flags, rc):
    m = "Connected flags" + str(flags) + "result code " \
        + str(rc) + "client1_id " + str(client)
    print(m)


client = mqtt.Client(config.deviceName"-PLAYER") #create new instance
client.connect(broker_address) #connect to broker
client.on_connect = on_connect
client.message_callback_add(topic,on_message)
print("Subscribing to topic",topic)
client.subscribe(topic)



client.on_message=on_message        #attach function to callback
client.loop_start()

while(True):
    time.sleep(100)
