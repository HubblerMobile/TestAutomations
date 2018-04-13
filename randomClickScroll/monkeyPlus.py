from automation_support import button, adbCmd, printMsg, setUp, \
    variables
from automation_support import TClogIn
import os
import time
from localUiautomator.uiautomator import device
from itertools import count
from random import random, randint


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
            while noElement:
                elementIndex = randint(0, elements.__len__() - 1)
                element = elements[elementIndex]
                elementProperty = element.info
                if elementProperty['clickable'] or elementProperty['longClickable'] or elementProperty['scrollable'] or \
                        elementProperty['focusable']:
                    noElement = False
                back = randint(0, 5)
                if back == 2:
                    #                     time.sleep(2)
                    print("-----asserting device back")
                    button.deviceBack()
                    elements = button.getAllEle()
            if elementProperty['clickable']:
                print("-----asserting click")
                element.click()
                wa = randint(0, 5)
                if wa == 1:
                    time.sleep(2)
                elements = button.getAllEle()
            elif elementProperty['longClickable']:
                print("-----asserting long-click")
                element.long_click()
                elements = button.getAllEle()
            elif elementProperty['scrollable']:
                up = randint(0, 1)
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
        cycle(elements)


def message():
    try:
        print("---------message start")
        button.message().click()
        time.sleep(2)
        elements = button.getAllEle()
        cycle(elements)
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("---------message test success")
    except Exception as e:
        print("---------message test fail")
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        pass


def notification():
    try:
        button.notification().click()
        time.sleep(2)
        elements = button.getAllEle()
        cycle(elements)
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("---------notification test pass")
    except Exception as e:
        print("---------notification test fail")
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        pass


def group():
    try:
        button.menu().click()
        button.findText("Grouup").click()
        time.sleep(2)
        elements = button.getAllEle()
        cycle(elements)
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("---------group test pass")
    except Exception as e:
        print("---------group test fail")
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        pass


def channel():
    try:
        button.menu().click()
        button.findText("Channel").click()
        time.sleep(2)
        elements = button.getAllEle()
        cycle(elements)
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("---------channel test pass")
    except Exception as e:
        print("---------channel test fail")
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        pass


def poll():
    try:
        button.menu().click()
        button.findText("Polls").click()
        time.sleep(2)
        elements = button.getAllEle()
        cycle(elements)
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("---------poll test pass")
    except Exception as e:
        print("---------poll test fail")
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        pass


def event():
    try:
        button.menu().click()
        button.findText("Events").click()
        time.sleep(2)
        elements = button.getAllEle()
        cycle(elements)
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("---------event test pass")
    except Exception as e:
        print("---------event test fail")
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        pass


def profile():
    try:
        button.menu().click()
        button.userProfilePage().click()
        time.sleep(2)
        elements = button.getAllEle()
        cycle(elements)
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("---------profile test pass")
    except Exception as e:
        print("---------profile test fail")
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        pass


def mainSearch():
    try:
        button.search().click()
        time.sleep(2)
        elements = button.getAllEle()
        cycle(elements)
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("---------mainserarch test pass")
    except Exception as e:
        print("---------mainSearch test fail")
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        pass


def action():
    message()
    print("message")
    mainSearch()
    print("main search")
    notification()
    print("notification")
    profile()
    print("profile")
    group()
    print("group")
    channel()
    print("channel")
    poll()
    print("poll")
    event()
    print("event")


def monkey():
    count = 0
    while count <= 20:
        adbCmd.runMonkey()
        count += 1
    count = 0


def menue():
    try:
        button.menu().click()
        time.sleep(2)
        count = 0
        while count <= 10:
            adbCmd.runMonkey()
            count += 1
    except Exception as e:
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        menue()


if __name__ == "__main__":
    adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
    action()
