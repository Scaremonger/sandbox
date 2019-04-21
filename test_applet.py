# MIoT Test Applet
#

# CONSTANTS
CONFIGFILE = "config.ini"   
# "/etc/opt/miot/miot_core.ini"
LISTEN = "miot"           # Where this module listens for instructions

# THIRD PARTY MODULES
import signal,sys,time
import paho.mqtt.client as paho_mqtt
import configparser as configParser

# CALLBACK / CONNACK
def on_connect( client, userdata, flags, rc ):
    print "Connected"
    if rc==0:    # Connected successfully
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe( LISTEN )
    else:
        print("Connection refused: Result code "+str(rc))
        if rc==1:
            print "  Incorrect protocol version"
        elif rc==2:
            print "  Invalid client identifier"
        elif rc==3:
            print "  Server unavailable"
        elif rc==4:
            print "  Bad username or password"
        elif rc==5:
            #logging.warning("MQTT, Not authorised")
            print "  Not authorised"
        else:
            print "Result code",rc

def on_disconnect( client, userdata, rc ):
    print "Disconnected, reason=",rc
    #logging.info("disconnecting reason  "  +str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message( client, userdata, msg ):
    print(msg.topic+"/"+str(msg.payload))

# CTRL-C Handler
def SIGINT( sig, frame ):
    print('You pressed Ctrl+C!')
    sys.exit(0)

# CONFIG FILE
config = configParser.ConfigParser()

# need try/fail here
config.read( CONFIGFILE )
if config.has_section( 'MQTT' ):
    mqtt_broker = config[ 'MQTT' ].get( 'broker', '127.0.0.1' )
    mqtt_port = config[ 'MQTT' ].getint( 'port', 1883 )
    mqtt_user = config[ 'MQTT' ].get( 'username' )
    mqtt_pass = config[ 'MQTT' ].get( 'password' )
else:
    print "MQTT Section missing from configuration file"
    mqtt_broker = '127.0.0.1'
    mqtt_port = 1883
   
print "MQTT"
print "broker:",mqtt_broker,":",mqtt_port

# INITIALISE MQTT
mqtt = paho_mqtt.Client()   # Use random client ID
if not mqtt_user=='':
    print "Authenticating as",mqtt_user
    mqtt.username_pw_set(username=mqtt_user,password=mqtt_pass)
mqtt.on_connect = on_connect
mqtt.on_disconnect = on_disconnect
mqtt.on_message = on_message
print "Connecting..."
try:
    mqtt.connect( mqtt_broker, mqtt_port )
except:
    print('connection failed')
    sys.exit(0)
signal.signal(signal.SIGINT, SIGINT)
print "Entering loop"
mqtt.loop_forever()
mqtt.disconnect()


