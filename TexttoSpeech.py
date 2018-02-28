# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:44:07 2018

@author: lenovo
"""
import random
import webbrowser
import os
import time
#import getpass
from gtts import gTTS
from mutagen.mp3 import MP3
import datetime

my_file = 'C:\\Users\\lenovo\\Desktop\\New folder\\hi.mp3' #Sets a variable for the file path.
#
#username = getpass.getuser() #Gets the username of the current user.

def removeFile():
    """Checks if myfile exists and if so, deletes."""
    if os.path.isfile(my_file):
        os.remove(my_file)

#hello how are you
        
def playTts():
    webbrowser.open(my_file)  # the converted file i.e. mp3 will be open.
    audio = MP3(my_file)  # Sets a variable so that the Mutagen module knows what file it's working with.
    audio_length = audio.info.length  # Sets a variable of the length of the .mp3 file.
    time.sleep(audio_length + 1.25)  # Waits until the file has finished playing.
    #os.system('TASKKILL /F /IM wmplayer.exe')  # Closes Windows Media Player.
    os.system('taskkill /f /im wmplayer.exe')
    time.sleep(0.5)  # Waits until Windows Media Player has closed.


def ask_and_play(speech):
    # Takes the user's input and uses it for the Text-To-Speech
    #speech = input('Hello '+username+"Enter the text:")
    
    tts = gTTS(text=speech, lang='en')
    tts.save('C:\\Users\\lenovo\\Desktop\\New folder\\hi.mp3')
    time.sleep(0.5)

    #tts.save('bob.mp3')  # Saves a .mp3 file of the user's input as speech.
    playTts()


def checkContinue():
    """Checks if the user wants to continue.
    Returns a boolean value."""
    while True:
        answer = input("Do you want to repeat? (Y/N) ").strip().lower()
        yes = ['yes', 'y']
        no = ['no', 'n']
        if answer in yes:
            return True
        elif answer in no :
            return False
        else:
            print("Sorry, I didn't understand that. Please try again with either Y or N.")
            ask_and_play("Sorry, I didn't understand that. Please try again with either Y or N.")
            #time.sleep(2)
            

def hi1(hi):
    speech = 'Bhai ' + random.choice(hi).capitalize()
    removeFile()
#    ask_and_play(speech)

    time.sleep(0.5)
    print("Garry Bot :",speech)      
    ask_and_play(speech)
 
def repeat():
    """Repeatedly ask the user to type text to play,
    and check if the user wants to repeat or exit."""
    hi = ["hello", "hi", "bonjour","namaste","good morning","good evening and how are you"]
    text = input("Say hi in your language:").lower()
    if text in hi:
        hi1(hi)
    else:
        speech = "Can't understand Please try again."
        ask_and_play(speech)
        hi1(hi)


    while True:
        speech = input('Hello '+"Enter the text:")
        removeFile()
        #print("Garry Bot")
        ask_and_play(speech)
        if not checkContinue():
            raise KeyboardInterrupt
#This is the change that I had make in my file            
if __name__ == '__main__':
    try:
        repeat() #Calls the function.
    except KeyboardInterrupt:
        # clean up
        removeFile()
        a = "Meet you soon!"
        print(a)
        ask_and_play(a)

