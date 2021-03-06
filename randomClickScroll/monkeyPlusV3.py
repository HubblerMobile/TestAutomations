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
        button.findText("Groups").click()
        time.sleep(2)
        monkey()
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("---------group test pass")
    except Exception as e:
        print(e)
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
    rou = 2
    count = 0
    
    while count <= rou:
        group()
        count += 1
    count = 0
    print("group")
    while count <= rou:
        channel()
        count += 1
    count = 0
    print("channel")
    while count <= rou:
        poll()
        count += 1
    count = 0
    print("poll")
    while count <= rou:
        event()
        count += 1
    count = 0
    print("event")
    while count <= rou:
        message()
        count += 1
    count = 0
    print("message")
    while count <= rou:
        mainSearch()
        count += 1
    count = 0
    print("main search")
    while count <= rou:
        notification()
        count += 1
    count = 0
    print("notification")
    while count <= rou:
        profile()
        count += 1
    count = 0
    print("profile")
    
def monkey():
    count = 0
    while count <= 1:
        adbCmd.runMonkey()
        count += 1
    count = 0    

if __name__=="__main__":
    adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
    action()