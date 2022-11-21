import pyautogui
from PIL import ImageGrab
import time
import cv2 as cv
import numpy as np
from random import randint, uniform


time.sleep(5)
print("Started")
# print(pyautogui.position())

# load on what to search on ss
fish_needle = cv.imread('fish1.png', cv.IMREAD_COLOR)
alert_needle = cv.imread('alert2.png', cv.IMREAD_GRAYSCALE)
jump_needle = cv.imread('jump1.png', cv.IMREAD_COLOR)
store_needle = cv.imread('store.png', cv.IMREAD_COLOR)

rod = 90

ax1 = 896
ay1 = 182
ax2 = 982
ay2 = 316


def checkJump():
    jump_ss = ImageGrab.grab(bbox=(1399, 688, 1825, 1100))
    jump_haystack = np.array(jump_ss)
    jump_haystack = cv.cvtColor(jump_haystack, cv.COLOR_RGB2BGR)
    result_jump = cv.matchTemplate(
        jump_haystack, jump_needle, cv.TM_CCOEFF_NORMED)
    jmin_val, jmax_val, jmin_loc, jmax_loc = cv.minMaxLoc(result_jump)
    return jmax_val


def checkStore():
    store_ss = ImageGrab.grab(bbox=(1268, 745, 1750, 913))
    store_haystack = np.array(store_ss)
    store_haystack = cv.cvtColor(store_haystack, cv.COLOR_RGB2BGR)
    result_store = cv.matchTemplate(
        store_haystack, store_needle, cv.TM_CCOEFF_NORMED)
    smin_val, smax_val, smin_loc, smax_loc = cv.minMaxLoc(result_store)
    return smax_val


def fixRod():
    print("fixRod called!")
    pyautogui.click(1749, 607)  # click the bag icon
    time.sleep(1)
    pyautogui.click(1370, 516)  # click repair icon
    time.sleep(1)
    pyautogui.click(1040, 805)  # click the 500 money icon
    time.sleep(1)
    pyautogui.click(833, 811)  # click yes
    time.sleep(1)
    pyautogui.click(833, 811)  # get out of bag
    time.sleep(1)


while True:
    # grabbing ss of the fish and alert
    fish_ss = ImageGrab.grab(bbox=(1399, 688, 1825, 1100))
    alert_ss = ImageGrab.grab(bbox=(ax1, ay1, ax2, ay2))

    # converting to openCv readable format
    fish_haystack = np.array(fish_ss)
    fish_haystack = cv.cvtColor(fish_haystack, cv.COLOR_RGB2BGR)
    alert_haystack = np.array(alert_ss)
    alert_haystack = cv.cvtColor(alert_haystack, cv.COLOR_RGB2GRAY)

    # match the image --- "find needle in the haystack"
    result_fish = cv.matchTemplate(
        fish_haystack, fish_needle, cv.TM_CCOEFF_NORMED)
    result_alert = cv.matchTemplate(
        alert_haystack, alert_needle, cv.TM_CCOEFF_NORMED)
    # get max match value -- for alert min gives most match
    amin_val, amax_val, amin_loc, amax_loc = cv.minMaxLoc(result_alert)
    fmin_val, fmax_val, fmin_loc, fmax_loc = cv.minMaxLoc(result_fish)

    if (rod == 0):
        fixRod()
        rod = 90

    if (fmax_val > 0.6):  # check if fish icon matches
        #print("In Water !!")
        if (amax_val > 0.5):  # check if fish is hooked
            print("Clicked reel/fish button!")
            # click the reel out(fish) button
            pyautogui.click(randint(1556, 1707), randint(806, 930))
            time.sleep(uniform(0.13, 0.1785714285714286))
            pyautogui.click(randint(1556, 1707), randint(806, 930))
            # time.sleep(uniform(0.13, 0.1785714285714286))
            # pyautogui.click(randint(1556, 1707), randint(806, 930))

        else:
            #print("Waiting for Fish.....")
            # print(amax_val)
            pass
    elif (checkJump() > 0.57):
        print("Throw hook clicked!")
        pyautogui.click(randint(1446, 1536), randint(
            659, 735))  # click the throw hook button
        time.sleep(2)
    elif (checkStore() > 0.7):
        pyautogui.click(1429, 848)
        print("Store clicked!")
        time.sleep(0.7)
        rod -= 1
        print(rod)
        if (rod == 0):
            fixRod()
            rod = 90
