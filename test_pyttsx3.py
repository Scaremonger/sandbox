# PYTTSX3 TEST PROGRAM
# https://github.com/nateshmbhat/pyttsx3
# https://pyttsx3.readthedocs.io/en/latest/engine.html#the-engine-factory

text = "High on a rocky promontory sat an Electric Monk on a bored horse."

import pyttsx3;
engine = pyttsx3.init();

def basic():
    engine.say(text);
    engine.runAndWait();
    engine.stop()

def voices():
    voices = engine.getProperty('voices')
    for voice in voices:
       engine.setProperty('voice', voice.id)
       print( voice.id,", ",voice.name,", ",voice.age,", ",voice.gender )
       engine.say('This is voice ',voice.name)
    engine.runAndWait()
    engine.stop()

def advanced():

    # CHANGE VOICE, RATE AND VOLUME

    # Rate (Default is 200)
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        #printing current voice rate
    #engine.setProperty('rate', 110)     # setting up new voice rate


    # Volume
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    print ("Volume:",volume)                          #printing current volume level
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    # Voice
    voice = engine.getProperty('voice')       #getting current voice
    print ("Voice:",voice)
    #voices = engine.getProperty('voices')       #getting details of current voice
    #print ("Voice:",voices)
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    #engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    engine.say(text)
    #engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    engine.stop()


# Examples
#basic()
#voices()
advanced()


