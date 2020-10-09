from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates () :
    replayBtn = (375,230)
    dinasaur = (86,250)
    #180= x Cordinates to check for tree
    #y Cordinates = 260

def restartGame () :
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSpace () :
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print ("Jump")
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab () :
    box = (Cordinates.dinasaur[0]+180,Cordinates.dinasaur[1],
           Cordinates.dinasaur[0]+285 ,Cordinates.dinasaur[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print (a.sum( ))
    return a.sum ( )

def main () :
    restartGame()
    while True :
        if(imageGrab()!=780) :
            pressSpace()
            time.sleep(0.5)

main ()

