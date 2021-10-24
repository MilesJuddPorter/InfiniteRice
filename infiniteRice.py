import pyautogui as p
import pytesseract
import numpy as np
import cv2
from mss import mss
from PIL import Image
import keyboard
import matplotlib.pyplot as plt
from time import sleep
import random

mon = {'left': 700, 'top': 200, 'width':425, 'height':300}
    

def getAnswer():
    scr = mss().grab(mon)
    img = np.array(scr)
    questionImg = img[0:110, 100:700]
    questionstr = pytesseract.image_to_string(questionImg)
    questionstr = questionstr.replace('\x0c', '').replace('[', '')
    questionstr = questionstr.replace('\n', '')
    questionstr = questionstr.replace(' ', '')
    number1, number2 = questionstr.split('x')
    answer = int(number1) * int(number2)
    return answer

def getOptions(answer):
    print(answer)
    scr = mss().grab(mon)
    img = np.array(scr)
    option1 = img[140:220, 300:500]
    option2 = img[280:350, 300:500]
    option3 = img[390:470, 300:500]
    option4 = img[510:580, 300:500]
    for ii, option in enumerate([option1, option2, option3, option4]):
        try:
            optionstr = pytesseract.image_to_string(option)
            optionstr = optionstr.replace('\x0c', '').replace('[', '')
            if answer == int(optionstr):
                return ii
        except:
            print(optionstr)

x = 900
while True:
    sleep(3)
    choice = getOptions(getAnswer())
    try:
        p.click(x, 300+(60*choice))
    except:
        randChoice = random.choice([0,1,2,3])
        p.click(x, 300+(60*randChoice))
        print("didnt get an answer, choosing randomly")