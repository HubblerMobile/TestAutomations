from automation_support import button, adbCmd, printMsg, setUp,\
    variables
from automation_support import TClogIn
import os
import time
from localUiautomator.uiautomator import device
from itertools import count

def action():
    try:
        count = 0
        while count <= 10:
            adbCmd.runMonkey()
            count += 1
        print("out of loop")
        a = 1/0
    except Exception as e:
        print(e)
        adbCmd.stopApp("mobi.hubbler.app")
        action()
        
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
#     adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
    action()