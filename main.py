import pyautogui
from PIL import ImageGrab
import time
import cv2 as cv
import numpy as np


time.sleep(5)
#img = ImageGrab.grab(bbox=(1493, 756, 1743, 1006))
# img.show()
print(pyautogui.position())


# load on what to search image
jmp_ss = ImageGrab.grab(bbox=(858, 259, 1007, 438))
jmp_haystack = np.array(jmp_ss)

# load img to be searched
jmp_needle = cv.imread('alert.png', cv.IMREAD_COLOR)

# match the image --- "find needle in the haystack"
result_jmp = cv.matchTemplate(jmp_haystack, jmp_needle, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result_jmp)
print("Max location = ", str(max_loc))
print("Max Value = " + str(max_val))

cv.imshow('Result', result_jmp)
cv.waitKey()
