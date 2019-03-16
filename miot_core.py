# PACKGE:   miot_core
# FILE:     miot_core.py
# HOME:     github.com/Scaremonger/miot/miot_core
# AUTHOR:   (c) Copyright Si.Dunford, 2019
# VERSION:  0.0.1
# DATE:     15 March 2019
# STATE:    Unfinished
# LICENSE:  tbc
#
# INSTALL:
# WILL EVENTUALL INSTALL SOMETHING LIKE THIS
#   pip install miot_core
#
# CHANGE LOG:
# 15 MAR 2019  0.0.1  Initial build
#
# Should be included in other miot packages as a dependency
#

import paho.mqtt.client as client
import configparser as configParser

# WRAPPER FOR CONFIGPARSER
class Config:
    def __init__( filename ):
        self.filename = filename
        self.config = configparser.ConfigParser

        # need try/fail here
        self.config.read( fielname )

    def get( item ):
        return "test"

# WRAPPER FOR PAHO MQTT
class MQTT:

    def __init__( host, port  ):
        self.host = host
        self.port = port

    def connect():
        client.connect( host, port )

    def on_connect( cb ):
        client.on_connect = cb

    def on_message( cb ):
        client.on_message = cb

    def forever():
        client.loop_forever()

# Initialise Configuration file
config = Config("/etc/opt/miot/miot_core.ini")

# Initialise MQTT and connect
mqtt = MQTT( config.get("MQTT_HOST"), config.get("MQTT_PORT") )


