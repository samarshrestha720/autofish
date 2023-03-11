from pyautogui import position
from time import sleep
# import cv2 as cv
# import numpy as np
# from PIL import ImageGrab
# from pytesseract import pytesseract

sleep(4)
print(position())

'''
name_needle = cv.imread('embr.png', cv.IMREAD_COLOR)
name_ss = ImageGrab.grab(bbox=(815, 374, 1081, 575))
name_haystack = np.array(name_ss)
name_haystack = cv.cvtColor(name_haystack, cv.COLOR_RGB2BGR)
result_name = cv.matchTemplate(
    name_haystack, name_needle, cv.TM_CCOEFF_NORMED)
smin_val, smax_val, smin_loc, smax_loc = cv.minMaxLoc(result_name)
print(smax_val, smin_val)
print(smax_loc)
name_ss.show()
'''
