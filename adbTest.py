#!/usr/bin/env python

import os
import time

stringTap = " adb shell input tap 300 300"
stringSwipe = "adb shell input swipe 500 300 500 1300 100"
i=0
while True:
    os.popen(stringTap)
    i=i+1
    print("first click " + str(i))
    time.sleep(1)