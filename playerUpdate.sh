#!/bin/bash
cd /opt
rm -rf mqttPlayer
sudo git clone https://github.com/antonagre/mqttPlayer
sudo cp config.py mqttPlayer/
startPlayer