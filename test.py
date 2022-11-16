import pyautogui
from time import sleep
import cv2 as cv
import numpy as np
from PIL import ImageGrab


sleep(4)
print(pyautogui.position())

'''
fish_needle = cv.imread('fish1.png', cv.IMREAD_COLOR)
alert_needle = cv.imread('alert.png', cv.IMREAD_COLOR)
jump_needle = cv.imread('jump1.png', cv.IMREAD_COLOR)

fish_ss = ImageGrab.grab(bbox=(1399, 688, 1825, 1100))
alert_ss = ImageGrab.grab(bbox=(848, 291, 1000, 397))
fish_haystack = np.array(fish_ss)
fish_haystack = cv.cvtColor(fish_haystack, cv.COLOR_RGB2BGR)
alert_haystack = np.array(alert_ss)
alert_haystack = cv.cvtColor(alert_haystack, cv.COLOR_RGB2BGR)

result_fish = cv.matchTemplate(
    fish_haystack, jump_needle, cv.TM_CCOEFF_NORMED)
result_alert = cv.matchTemplate(
    alert_haystack, alert_needle, cv.TM_CCOEFF_NORMED)

amin_val, amax_val, amin_loc, amax_loc = cv.minMaxLoc(result_alert)
fmin_val, fmax_val, fmin_loc, fmax_loc = cv.minMaxLoc(result_fish)

print("alert value: ", amax_val)
print("fish value: ", fmax_val)
'''
