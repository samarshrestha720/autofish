import pyautogui
import time

time.sleep(5)
# print(pyautogui.position())
im1 = pyautogui.screenshot(region=(867, 241, 200, 300))
im1.save(r"C:\Users\lenev\OneDrive\Documents\pt_autofish\test1.png")
