#-*- coding: UTF-8 -*-
__author__ = '007'
__date__ = '2016/4/7'

from tkinter import *

from PIL import Image, ImageTk
import os
import time

import _thread
import json
PATH = lambda p: os.path.abspath(p)

adbpush = "adb push "
global label_img
global img_pngl
adbpushwhere = " /system/framework/arm64/"

aline = "\n__________________________________________________________________________________________\n"
#______________________________________________________________________________________________________
root = Tk() # 初始化Tk()
root.title("仅陈卓-用来调试Android")    # 设置窗口标题
root.geometry()    # 设置窗口大小 注意：是x 不是*
def printline():
    print("__________________________________________________________________________________________\n")


def printhello():
    t.insert(END,"hello\n")
    t.see(END)

def printSomeWords(inputString):
    t.insert(END,inputString + '\n')
    t.see(END)


def testGetCapture():

    print("testGEt")

#获取截图
def getCapture():

    print("getCapture START")
    printSomeWords("截图-")
    tempImage = screenshot();
    print("getImageName is " + tempImage)
    time.sleep(2.5)
    showAimage(tempImage);

    print("getCapture END")
# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

def throwThreadgetCapture():
    # 创建两个线程
    try:
        _thread.start_new_thread(getCapture,())
        #_thread.start_new_thread(print_time, ("Thread-1", 2,))
    except:
        print("Error: 无法启动线程")

#获取设备信息
def getDevices():


    printSomeWords("获取设备信息-")
    deviceInfo =  androidDevice();

    printSomeWords(str(deviceInfo))


#获取SCCARD/LOGS 的日志

def getSDCARDLOGS():
    printSomeWords("获取设备的SDCARD/LOGS日志")
    path = PATH(os.getcwd() + "/SDCARDLOGS")



    if not os.path.isdir(PATH(os.getcwd() + "/SDCARDLOGS")):
        os.makedirs(path)


    time.sleep(3.5)
    #tempopen = os.popen(r"adb pull /sdcard/logs/ " + PATH(path),"r",).readlines()
    tempopen = os.popen(r"adb pull /sdcard/logs/ " + PATH(path), "r", )
    #;;;;
    tempString = tempopen.read()
    print("getSOme",tempString)
    print(tempopen)
    #printSomeWords(str(tempString))

#截图CMD命令
def screenshot():
    path = PATH(os.getcwd() + "/screenshot")

    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    #os.popen("adb wait-for-device")
    os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
    if not os.path.isdir(PATH(os.getcwd() + "/screenshot")):
        os.makedirs(path)


    time.sleep(3.5)
    tempopen = os.popen("adb pull /data/local/tmp/tmp.png " + PATH(path + "/" + timestamp + ".png"))

    print(tempopen)
    #time.sleep(2)
    os.popen("adb shell rm /data/local/tmp/tmp.png")
    print("success")
    return PATH(path + "/" + timestamp + ".png")
#设备信息CMD命令
def androidDevice():
    tempopen = os.popen("adb devices")
    haha =tempopen.read()
    print("haha="+ haha);
    return haha



def slimUp():
    stringSwipe = "adb shell input swipe 500 300 500 1300 100"
    os.popen(stringSwipe)
    printSomeWords("向上滑动——————————————————————————————————")

def slimDown():
    stringSwipe = "adb shell input swipe 500 1300 500 300 100"
    os.popen(stringSwipe)
    printSomeWords("向下滑动——————————————————————————————————")

def resize(w, h, w_box, h_box, pil_image):
  '''
  resize a pil_image object so it will fit into
  a box of size w_box times h_box, but retain aspect ratio
  对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
  '''
  f1 = 1.0*w_box/w # 1.0 forces float division in Python2
  f2 = 1.0*h_box/h
  factor = min([f1, f2])
  #print(f1, f2, factor) # test
  # use best down-sizing filter
  width = int(w*factor)
  height = int(h*factor)
  return pil_image.resize((width, height), Image.ANTIALIAS)


#C:\Users\chenzhuo\PycharmProjects\AndroidS\screenshot\2018-11-30-10-02-50.png


def showAimage(filename):
    pass
    global label_img
    global img_pngl
    img_pngl = PhotoImage(file=str(filename))

    img_pngl = img_pngl.subsample(3, 3)
    # 获取图像的原始大小


    label_img.configure(image = img_pngl)

    # pil_image_resized = img_png.zoom( w_box,h_box)

    # label_img = Label(root, image = img_png )


    #global  label_img.configure(img_png)
    #
img_png = PhotoImage(file='''haha.png''')

img_png = img_png.subsample(3,3)
#获取图像的原始大小




#pil_image_resized = img_png.zoom( w_box,h_box)

#label_img = Label(root, image = img_png )

label_img = Label(root, image = img_png ,width = 480 ,height = 680 )
label_img.grid(row = 0, column = 3 ,columnspan =2)



t = Text()
# t.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
# Button(root, text="press", command=printhello).pack()
#
#
# Button(root, text="截图", command=getCapture).pack()
# Button(root, text="设备信息", command=getDevices).pack()
t.grid(row = 0, column = 0 ,columnspan =3)
Button(root, text="打印一个Hello", command=printhello).grid(row = 1, column = 0)
Button(root, text="截图", command=throwThreadgetCapture).grid(row = 1, column = 1)

Button(root, text="向上滑动屏幕", command=slimUp).grid(row = 1, column = 2)


Button(root, text="设备信息", command=getDevices).grid(row = 2, column = 0)
Button(root, text="获取/SCARD/LOGS的日志", command=getSDCARDLOGS).grid(row = 2, column = 1)

Button(root, text="向下滑动屏幕", command=slimDown).grid(row = 2, column = 2)
root.mainloop() # 进入消息循环