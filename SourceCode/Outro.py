import os
import time
import keyboard as keyboard

file = "outroMusic.wav"
os.system(file)

time.sleep(0.2)
keyboard.press_and_release("alt + tab")
time.sleep(0.2)
keyboard.press_and_release("f11")
time.sleep(0.1)

for i in range(10, 0, -1):
    print("Shutting down in..." + str(i))
    time.sleep(1)

time.sleep(1.5)

os.system("shutdown /s /t 0")
