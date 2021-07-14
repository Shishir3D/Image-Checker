from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(5)
a = 1

while 1:
        if pyautogui.locateOnScreen('ss.png', region=(2,300,300,700), confidence=0.99) != None:
            visible = "I can see it"
            time.sleep(5)
            pyautogui.press("f5")
        else:
            visible = "I am unable to see it"
            time.sleep(5)
            break

if visible == "I am unable to see it":
                click(200,30)
                time.sleep(1)
                pyautogui.press("space")
                
