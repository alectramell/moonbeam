import os
import random

def refresh():
    keys = raw_input('Git Project: ')
    keys = keys.encode("hex")
    keystring = open("data","w")
    keystring.write(keys)
    keystring.close()
    
def getkey():
    slate = open("data","r")
    key = slate.read()
    slate.close()
    key = key.decode("hex")
    os.system('zenity --title="APOLLON | GitHub Request" --info --text="http://github.com/alectramell/' + key + '.git"')
    os.system("cd ~/Desktop/ && git clone https://github.com/alectramell/" + key + ".git")
    os.system("clear")
    print ("DONE!")
    os.system("sleep 3 && clear")
    os.system("gnome-open ~/Desktop/" + key + "/")
    
