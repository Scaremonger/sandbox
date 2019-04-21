# Modular Internet of Things, MQTT TTS interface
#
# FILE:     miot_mqtt_tts.py
# AUTHOR:   (c) Copyright Si.Dunford, 2019
# VERSION:  1.3
# DATE:     26 March 2019
# STATE:    BETA
# LICENSE:  MIT License
#
# PURPOSE:
# Listen on MQTT topic for speech instructions.
# The module allows you to control volume and speech rate.
#
# PRE-REQUISITES:
#   pip install pyttsx3
#
# CHANGES
# 26 Mar 2019  1.0  Initial Version
#              1.1  Added action=rate, action=volume (including save)
#              1.2  Added action=reset
#              1.3  Added support for non JSON text to speech.

# LIBRARY
import json
import pyttsx3;
from miot_core import mqtt, config
engine = pyttsx3.init();

# DEFAULTS
speech_rate = config.getint( 'mqtt_tts', 'rate', 150 )
speech_volume = config.getfloat( 'mqtt_tts', 'volume', 1.0 )

# CALLBACK
def on_message( client, userdata, msg ):
    global engine, config, speech_rate, speech_volume

    # Extract request from payload
    try:
        data = json.loads( msg.payload )
    except ValueError, e:
        # Message payload is TEXT, so convert it!
        data = {}
        data['text'] = msg.payload 
    #print(msg.topic+"/"+str(msg.payload))
    #for x in data:
    #    print(x+": "+data[x])

    # Process command actions
    if 'action' in data:
        action = data['action']
        #print "ACTION: "+action
        #if action=='stop':
        #    engine.stop()
        #    return
        if action=='mute':
            speech_volume = 0.0
            return
        if action=='volume':
            if not "volume" in data:
                return
            # Volume is specified 0 to 10, but module needs 0 to 1
            speech_volume = float( data['volume'] )
            speech_volume = speech_volume / 10.0
            if speech_volume>1.0:
                speech_volume = 1.0
            # Save this setting for future re-load
            config.set( "mqtt_tts", "volume", str(speech_volume) )
            config.write()
            return
        if action=='rate':
            if not "rate" in data:
                return
            speech_rate = int( data['rate'] )
            # Save this setting for future re-load
            config.set( "mqtt_tts", "rate", str(speech_rate) )
            config.write()
            return
        if action=='reset':
            speech_rate = 150
            speech_volume = 1.0
            config.set( "mqtt_tts", "rate", "150" )
            config.set( "mqtt_tts", "volume", "1.0" )
            config.write()
            return

    # The default action is to speak!
    #print "ACTION: speak"

    if not "text" in data or data['text']=='':
        print "- No text specified"
        # No text to speak!
        return

    # Set defaults
    text = data['text']
    rate = speech_rate
    volume = speech_volume

    # Override default settings
    if "volume" in data:
        volume = float( data['volume'] )
        volume = volume / 10.0
        if volume>1.0:
            volume = 1.0

    if "rate" in data:
        rate = int( data['rate'] )

    # Speak
    #print 'SAY (vol='+str(volume)+',rate='+str(rate)+'), "'+text+'"'
    engine.setProperty( 'rate', rate )
    engine.setProperty( 'volume', volume )
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Initialise module
topic = config.get( 'mqtt_tts', 'topic', 'miot/tts' )
print "MQTT TTS"
print "BROKER=",mqtt.broker+":"+str(mqtt.port)
print "TOPIC= ",topic
mqtt.forever( topic, on_message )




