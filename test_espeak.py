# ESPEAK TEST PROGRAM

text = "High on a rocky promontory sat an Electric Monk on a bored horse."

from espeak import espeak

#espeak.set_voice("ru")
#espeak.synth("")

espeak.synth(text);

while espeak.is_playing:
	pass


#import os
#os.system("espeak 'The quick brown fox'")


