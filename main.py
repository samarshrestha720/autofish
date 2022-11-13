#import pyautogui
from PIL import ImageGrab
import time
import cv2 as cv
import numpy as np


time.sleep(5)
#img = ImageGrab.grab(bbox=(1493, 756, 1743, 1006))
# img.show()
# print(pyautogui.position())

fish_needle = cv.imread('fish.png', cv.IMREAD_COLOR)
alert_needle = cv.imread('alert.png', cv.IMREAD_COLOR)

while True:
    fish_ss = ImageGrab.grab(bbox=(1399, 688, 1825, 1100))
    fish_haystack = np.array(fish_ss)
    alert_ss = ImageGrab.grab(bbox=(902, 289, 964, 389))
    alert_haystack = np.array(alert_ss)
    # load on what to search image
    # jmp_ss = ImageGrab.grab(bbox=(1399, 688, 1825, 1100))
    # jmp_haystack = np.array(jmp_ss)

    # # load img to be searched
    # jmp_needle = cv.imread('fish.png', cv.IMREAD_COLOR)

    # match the image --- "find needle in the haystack"
    result_fish = cv.matchTemplate(
        fish_haystack, fish_needle, cv.TM_CCOEFF_NORMED)
    result_alert = cv.matchTemplate(
        alert_haystack, alert_needle, cv.TM_SQDIFF_NORMED)
    amin_val, amax_val, amin_loc, amax_loc = cv.minMaxLoc(result_alert)
    fmin_val, fmax_val, fmin_loc, fmax_loc = cv.minMaxLoc(result_fish)
    if (fmax_val > 0.6):
        print("In Water !!")
        if (amin_val < 0.2):
            print("Fish hooked!!! Reel in Fast!!")
        else:
            print("Waiting for Fish.....")
    else:
        print("Please throw hook in water!")
