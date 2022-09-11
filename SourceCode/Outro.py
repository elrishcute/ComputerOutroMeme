import os
import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # sorry Pygame community :(
import pygame
import keyboard as keyboard
from pygame import mixer

if not os.path.exists("outroMusic.wav"): # check for the music file
    print("THE MUSIC (outroMusic.wav) IS MISSING")

else:
    outrosound = os.path.join(os.getcwd(), 'outroMusic.wav') # filename
    mixer.init()
    mixer.music.load(outrosound)
    mixer.music.play()

    time.sleep(0.2)
    keyboard.press_and_release("f11") # fullscreen the terminal
    time.sleep(0.1)

    for i in range(10, 0, -1):
        print("Shutting down in..." + str(i))
        time.sleep(1)

    time.sleep(1.5)

    os.system("shutdown /s /t 0")
