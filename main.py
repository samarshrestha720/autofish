import pyautogui
from PIL import ImageGrab
import time
import cv2 as cv
import numpy as np


time.sleep(5)

# print(pyautogui.position())

# load on what to search on ss
fish_needle = cv.imread('fish.png', cv.IMREAD_COLOR)
alert_needle = cv.imread('alert.png', cv.IMREAD_COLOR)
jump_needle = cv.imread('jump.png', cv.IMREAD_COLOR)


def checkJump():
    jump_ss = ImageGrab.grab(bbox=(1399, 688, 1825, 1100))
    jump_haystack = np.array(jump_ss)
    jump_haystack = cv.cvtColor(jump_haystack, cv.COLOR_RGB2BGR)
    result_jump = cv.matchTemplate(
        jump_haystack, jump_needle, cv.TM_CCOEFF_NORMED)
    jmin_val, jmax_val, jmin_loc, jmax_loc = cv.minMaxLoc(result_jump)
    return jmax_val


while True:
    # grabbing ss of the fish and alert
    fish_ss = ImageGrab.grab(bbox=(1399, 688, 1825, 1100))
    alert_ss = ImageGrab.grab(bbox=(902, 289, 964, 389))

    # converting to openCv readable format
    fish_haystack = np.array(fish_ss)
    fish_haystack = cv.cvtColor(fish_haystack, cv.COLOR_RGB2BGR)
    alert_haystack = np.array(alert_ss)
    alert_haystack = cv.cvtColor(alert_haystack, cv.COLOR_RGB2BGR)

    # match the image --- "find needle in the haystack"
    result_fish = cv.matchTemplate(
        fish_haystack, fish_needle, cv.TM_CCOEFF_NORMED)
    result_alert = cv.matchTemplate(
        alert_haystack, alert_needle, cv.TM_SQDIFF_NORMED)
    # get max match value -- for alert min gives most match
    amin_val, amax_val, amin_loc, amax_loc = cv.minMaxLoc(result_alert)
    fmin_val, fmax_val, fmin_loc, fmax_loc = cv.minMaxLoc(result_fish)

    if (fmax_val > 0.6):  # check if fish icon matches
        print("In Water !!")
        if (amin_val < 0.2):  # check if fish is hooked
            print("Fish hooked!!! Reel in Fast!!")
            pyautogui.click(1581, 827)  # click the reel out(fish) button
        else:
            print("Waiting for Fish.....")
    elif (checkJump() > 0.6):
        print("Throwing hook in water!")
        pyautogui.click(1466, 693)  # click the throw hook button
    else:
        pyautogui.click(1290, 855)
        time.sleep(0.5)
