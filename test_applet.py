# MIoT Test Applet
#

# MIOT_CORE

#from miot_core import mqtt,config
from miot_core import mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqtt.on_connect = on_connect
mqtt.on_message = on_message

# Connect to MQTT server and loop forever
mqtt.forever()
