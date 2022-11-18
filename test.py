import pyautogui
from time import sleep
import cv2 as cv
import numpy as np
from PIL import ImageGrab


sleep(4)
print(pyautogui.position())
'''
store_needle = cv.imread('store.png', cv.IMREAD_COLOR)
store_ss = ImageGrab.grab(bbox=(1268, 745, 1750, 913))
store_haystack = np.array(store_ss)
store_haystack = cv.cvtColor(store_haystack, cv.COLOR_RGB2BGR)
result_store = cv.matchTemplate(
    store_haystack, store_needle, cv.TM_CCOEFF_NORMED)
smin_val, smax_val, smin_loc, smax_loc = cv.minMaxLoc(result_store)
print(smax_val)
'''
