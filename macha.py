from pyautogui import click, position
from PIL import ImageGrab
from time import sleep
import cv2 as cv
import numpy as np
from random import randint, uniform
from datetime import datetime
from PyQt6.QtCore import QObject, pyqtSignal


class fishy(QObject):
    operation_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()  # call the base class constructor

        # load on what to search on ss
        self.fish_needle = cv.imread('fish1.png', cv.IMREAD_COLOR)
        self.alert_needle = cv.imread('alert2.png', cv.IMREAD_GRAYSCALE)
        self.jump_needle = cv.imread('jump1.png', cv.IMREAD_COLOR)
        self.store_needle = cv.imread('store1.png', cv.IMREAD_COLOR)

        self.start_time = datetime.now()  # record script start time

        # initialize
        self.rod = 0  # record number of fish catched
        self.count = 0  # used to check when to trigger fixRod
        self.fixCount = 0  # record how many times fixRod has been called

        print("Initialization Complete!")

    def get_cords(self):
        sleep(4)
        return str(position())

    def checkJump(self):
        #jump_ss = ImageGrab.grab(bbox=(1399, 688, 1825, 1100))
        jump_ss = ImageGrab.grab(bbox=(1509, 763, 1731, 976))
        jump_haystack = np.array(jump_ss)
        jump_haystack = cv.cvtColor(jump_haystack, cv.COLOR_RGB2BGR)
        result_jump = cv.matchTemplate(
            jump_haystack, self.jump_needle, cv.TM_CCOEFF_NORMED)
        _, jmax_val, _, _ = cv.minMaxLoc(result_jump)
        return jmax_val

    def checkStore(self):
        store_ss = ImageGrab.grab(bbox=(1261, 818, 1728, 896))
        store_haystack = np.array(store_ss)
        store_haystack = cv.cvtColor(store_haystack, cv.COLOR_RGB2BGR)
        result_store = cv.matchTemplate(
            store_haystack, self.store_needle, cv.TM_CCOEFF_NORMED)
        _, smax_val, _, _ = cv.minMaxLoc(result_store)
        return smax_val

    def fixRod(self):
        print("fixRod called!")
        click(1753, 634)  # click the bag icon
        sleep(1.5)
        click(1370, 516)  # click repair icon
        sleep(1.5)
        click(1040, 805)  # click the 500 money icon
        sleep(1.5)
        click(833, 811)  # click yes
        sleep(1.5)
        click(833, 811)  # get out of bag
        sleep(1)

    def run(self, cord1, cord2):
        # coordinates of where to check for "!" mark
        self.cord1 = str(cord1)
        self.cord2 = str(cord2)
        # get coordinates from cord1&cord2 and place
        self.ax1 = int(
            self.cord1[self.cord1.find("x=")+2:self.cord1.find(",")])
        self.ay1 = int(
            self.cord1[self.cord1.find("y=")+2:self.cord1.find(")")])
        self.ax2 = int(
            self.cord2[self.cord2.find("x=")+2:self.cord2.find(",")])
        self.ay2 = int(
            self.cord2[self.cord2.find("y=")+2:self.cord2.find(")")])
        sleep(2)
        print("Started!!")
        self.operation_signal.emit(f"Started!!")
        while (self.fixCount < 4):
            '''elapsed_time = datetime.now()-start_time
            if (elapsed_time.total_seconds() > 900):
                sleep(899)
                start_time = datetime.now()'''

            # grabbing ss of the fish and alert
            #fish_ss = ImageGrab.grab(bbox=(1399, 688, 1825, 1100))
            fish_ss = ImageGrab.grab(bbox=(1509, 763, 1731, 976))
            alert_ss = ImageGrab.grab(
                bbox=(self.ax1, self.ay1, self.ax2, self.ay2))

            # converting to openCv readable format
            fish_haystack = np.array(fish_ss)
            fish_haystack = cv.cvtColor(fish_haystack, cv.COLOR_RGB2BGR)
            alert_haystack = np.array(alert_ss)
            alert_haystack = cv.cvtColor(alert_haystack, cv.COLOR_RGB2GRAY)

            # match the image --- "find needle in the haystack"
            result_fish = cv.matchTemplate(
                fish_haystack, self.fish_needle, cv.TM_CCOEFF_NORMED)
            result_alert = cv.matchTemplate(
                alert_haystack, self.alert_needle, cv.TM_CCOEFF_NORMED)
            # get max match value -- for alert min gives most match
            _, amax_val, _, _ = cv.minMaxLoc(result_alert)
            _, fmax_val, _, _ = cv.minMaxLoc(result_fish)

            if (fmax_val > 0.7):  # check if fish icon matches
                #print("In Water !!")
                if (amax_val > 0.6):  # check if fish is hooked
                    print("Clicked reel/fish button!")
                    # click the reel out(fish) button
                    #click(randint(1556, 1707), randint(806, 930))
                    click(randint(1557, 1694), randint(811, 940))
                    sleep(uniform(0.13, 0.1785714285714286))
                    click(randint(1557, 1694), randint(811, 940))
                    # sleep(uniform(0.13, 0.1785714285714286))
                    # click(randint(1556, 1707), randint(806, 930))

                else:
                    #print("Waiting for Fish.....")
                    # print(amax_val)
                    pass
            elif (self.checkJump() > 0.5):
                print("Throw hook clicked!")
                '''click(randint(1446, 1536), randint(
                    659, 735))'''  # click the throw hook button
                click(randint(1452, 1528), randint(
                    659, 736))
                self.count += 1
                sleep(2.1)
                if (self.count > 2):
                    self.fixRod()
                    self.fixCount += 1
                    self.count = 0
            elif (self.checkStore() > 0.7):
                click(1429, 848)
                print("Store clicked!")
                sleep(0.7)
                self.rod += 1
                self.count = 0
                self.fixCount = 0
                print(self.rod, self.fixCount)
                self.operation_signal.emit(f"Fish:{self.rod}")
        if (self.fixCount == 4):
            print("STOPPED!! FIX ROD CALLED TOO MANY TIMES!")
            self.operation_signal.emit(
                "STOPPED!! FIX ROD CALLED TOO MANY TIMES!")

    def stop(self):
        self.fixCount = 5
