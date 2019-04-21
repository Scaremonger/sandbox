
# Modular Internet of Things, WHEN engine
#
# FILE:     miot_when.py
# AUTHOR:   (c) Copyright Si.Dunford, 2019
# VERSION:  1.0
# DATE:     26 March 2019
# STATE:    BETA
# LICENSE:  MIT License
#
# PURPOSE:
# Object-Profile based Event manager
#
# PRE-REQUISITES:
#   
#
# CHANGES
# 26 Mar 2019  1.0  Initial Version
#

# Based on code found at:
# https://forum.xda-developers.com/showthread.php?t=2637556

#
#" ""
#Each "rule" has a "when" field, that contains a number of triggers.
#The "when" field activates when all the triggers are true, causing the "action" #to occur

#When a message arrives on MQTT, do I pass it to each trigger for review?
#Do I pass it only to MQTT triggers?

#I need a hook into the time and perfrom date etc events.

#Actions will be:
#    * Publish MQTT (topic, message, qos, will, using variable replacement)
#    * Set/Clear soft variable
#    * Syslog
#    * Message Log
#    * Console output (Only useful during debugging, but hey).

Triggers are a combination of an MQTT object and a comparison

    The topics in each trigger are subscribed on load (or addition)
    When a message arrived from MQTT, it is passed to every object
    The object compares the topic and any variables in the payload.
    ( I need to create a regex to do this when the topic is created)
    If there is a match; the object is informed. It must compare the
    result and set a changed flag, saving the old value and updating itself.
    It must then perform the comparison in the trigger (Changed, >, < contains, etc)
    and it updates it's staus. The rule is informed and it checks all triggers
    and it the rule changes state, it is added to an action list.
    Once the trigger is processed, the state chnages are processed which may cause 
    further actions to be added to the list.
    Next, the actions are processed in order, which may, in turn update soft-variables

"" "


