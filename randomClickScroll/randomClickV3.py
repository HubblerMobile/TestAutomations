from automation_support import button, adbCmd, printMsg, setUp,\
    variables
from automation_support import TClogIn
import os
import time
from localUiautomator.uiautomator import device
from pprint import pprint
from random import random, randint
from adbCmd import adb

def backLoop(count):
    print("-----asserting device back")
    if count > 5:
        return
    button.deviceBack()
    time.sleep(2)
    elements = button.getAllEle()
    if elements.__len__() > 0:
        cycle(elements)
    else:
        count += 1
        backLoop(count)
    return

def cycle(elements):
    
    try:
        count = 0
        while count <= 20:
            count += 1
#             print("length of array : ",elements.__len__())
            noElement = True
            while noElement :
                elementIndex = randint(0,elements.__len__()-1)
                element = elements[elementIndex]
                elementProperty = element.info
                if elementProperty['clickable'] or elementProperty['longClickable'] or elementProperty['scrollable'] or elementProperty['focusable']:
                    noElement = False
                back = randint(0,5)
                if back == 2:
#                     time.sleep(2)
                    print("-----asserting device back")
                    button.deviceBack()
                    elements = button.getAllEle()
            if elementProperty['clickable']:
                print("-----asserting click")
                element.click()
                wa = randint(0,5)
                if wa == 1:
                    time.sleep(2)
                elements = button.getAllEle()
            elif elementProperty['longClickable']:
                print("-----asserting long-click")
                element.long_click()
                elements = button.getAllEle()
            elif elementProperty['scrollable']:
                up = randint(0,1)
                if up == 1:
                    element.scroll.vert.forward(steps=10)
                    print("-----asserting forward scroll")
                else:
                    element.scroll.vert.backward(steps=10)
                    print("-----asserting backward scroll")
                elements = button.getAllEle()
            elif elementProperty['focusable']:
                print("-----asserting focus")
                element.click()
                element.set_text("some")
                elements = button.getAllEle()
        print("out of loop")
#         backLoop(0)
#         raise ValueError('mannual exception')
    except Exception as e:
        adbCmd.stopApp("mobi.hubbler.app")
        print(e)
        print(">>>>>>>>>>>some exception happened")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        elements = button.getAllEle()
        print(elements[0].info)
#         cycle(elements)
    

if __name__=="__main__":
    adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
    elements = button.getAllEle()
    print(elements[0].info)
    cycle(elements,0)
