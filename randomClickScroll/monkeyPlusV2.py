from automation_support import button, adbCmd, printMsg, setUp,\
    variables
from automation_support import TClogIn
import os
import time
from localUiautomator.uiautomator import device
from itertools import count
from random import random, randint

def message():
    try:
        print("---------message start")
        button.message().click()
        time.sleep(2)
        monkey()
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
        monkey()
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
        monkey()
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
        monkey()
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
        monkey()
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
        monkey()
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
        monkey()
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
        monkey()
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
if __name__=="__main__":
    adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
    action()