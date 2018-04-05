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
        cycle(elements,0)
    elementCount = elements.__len__()
    if elementCount <= 0:
        count += 1
        backLoop(count)
    return

def cycle(elements,count):
    try:
        if count > 500:
            return
        elementCount = elements.__len__()
        "if elementCountght value is 0 it means control is out of hubbler app. To get control back in hubbler app loop of device back is used"
        if elementCount == 0:
            backLoop(0)
        "randomly selecting one elementment to click"
        noElement = True
        while noElement :
            elementIndex = randint(0,elementCount-1)
            element = elements[elementIndex]
            elementProperty = element.info
            if elementProperty['clickable'] or elementProperty['longClickable'] or elementProperty['scrollable'] or elementProperty['focusable']:
                noElement = False
            back = randint(0,5)
            if back == 2:
                time.sleep(2)
                print("-----asserting device back")
                button.deviceBack()
        if elementProperty['text']:
            print("text : ",elementProperty['text'])
        if elementProperty['contentDescription']:
            print("description : ",elementProperty['contentDescription'])
        if elementProperty['clickable']:
            print("-----asserting click")
            count +=1
            element.click()
            elements = button.getAllEle()
            cycle(elements,count)
        if elementProperty['longClickable']:
            print("-----asserting long-click")
            count +=1
            element.long_click()
            elements = button.getAllEle()
            cycle(elements,count)
        if elementProperty['scrollable']:
            count +=1
            up = randint(0,1)
            if up == 1:
                element.scroll.vert.forward(steps=10)
                print("-----asserting forward scroll")
            else:
                element.scroll.vert.backward(steps=10)
                print("-----asserting backward scroll")
            elements = button.getAllEle()
            cycle(elements,count)
        if elementProperty['focusable']:
            print("-----asserting focus")
            element.click()
            element.set_text("some")
            elements = button.getAllEle()
            cycle(elements,count)
        cycle(elements,count)
    except Exception as e:
        adbCmd.stopApp("mobi.hubbler.app")
        print(e)
        print(">>>>>>>>>>>some exception happened")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        elements = button.getAllEle()
        print(elements[0].info)
        cycle(elements,0)
    

if __name__=="__main__":
    adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
    elements = button.getAllEle()
    print(elements[0].info)
    cycle(elements,0)
