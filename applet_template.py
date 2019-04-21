# Modular Internet of Things, Applet Template
#
# FILE:     applet_template.py
# AUTHOR:   (c) Copyright Si.Dunford, 2019
# VERSION:  1.0
# DATE:     26 March 2019
# STATE:    BETA
# LICENSE:  MIT License
#

# LIBRARY
import json
from miot_core import mqtt
#from miot_core import config
#speach_rate = config.getint( 'mqtt_tts', 'rate', 150 )

# CALLBACK
def on_message( client, userdata, msg ):
    print(msg.topic+"/"+str(msg.payload))
        
    # Extract JSON request
    #data = json.loads( msg.payload )
    #for x in data:
    #    print(x+": "+data[x])

print "MQTT TEST APPLET"
print "BROKER=",mqtt.broker+":"+str(mqtt.port)

# Optionally set the client ID, default is a random string
#mqtt.clientid = 'My_Client'

# Optionally set the topic
#mqtt.topic = 'miot/somewhere'
#mqtt.on_message = on_message
#mqtt.forever()

# Override event handlers
#mqtt.on_connect = on_connect
#mqtt.on_disconnect = on_disconnect
#mqtt.on_message = on_message
#mqtt.on_publish = on_publish
#mqtt_on_subscribe = on_subscribe 
#mqtt.forever( 'miot' )

# All-in-one call to start MIOT
mqtt.forever( 'miot', on_message )




