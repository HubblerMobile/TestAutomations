from automation_support import button, adbCmd, printMsg, setUp,\
    variables
from automation_support import TClogIn
import os
import time
from localUiautomator.uiautomator import device

def action():
    s= variables.s
    
    resp = []
    try:
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("\n\n")
        print("------user profile-----")
        button.menu().click()
        print("--drawe opened")
        button.drawerHeader().click()
        print("--user profile opend from drawer")
        time.sleep(1)
        button.findTextContain("manish@kumar.com").click()
        print("--user's email id clicked")
        time.sleep(1)
        button.deviceBack()
        button.findTextContain("1222333444").click()
        print("--user's phone number clicked")
        time.sleep(1)
        button.deviceBack()
        button.findTextContain("Following").click()
        print("--user's following list is opened")
        time.sleep(2)
        button.listView().fling.toEnd()
        button.listView().fling.toBeginning()
        print("--scrolled in user's following list")
        button.enterText("Aadarsh")
        print("--text entered in search box in following list")
        button.enterText("",True)
        button.listView().child_by_instance(1).click()
        print("--following's profile opened")
        time.sleep(1)
        button.deviceBack()
        button.appBack().click()
        print("--app back button clicked in following list")
        button.findTextContain("followers").click()
        print("--user's followers list is opened")
        time.sleep(2)
        button.listView().fling.toEnd()
        button.listView().fling.toBeginning()
        print("--scrolled in user's follower list")
        button.enterText("Aadarsh")
        print("--text entered in search box in followers lsit")
        button.enterText("", True)
        button.listView().child_by_instance(1).click()
        print("--follower's profile opened")
        time.sleep(1)
        button.deviceBack()
        button.appBack().click()
        print("--app back button clicked in followers list")
        button.listView().fling.toEnd()
        button.listView().fling.toBeginning()
        button.listView().fling.toBeginning()
        print("--scrolled in profile")
        button.backUserProfile().click()
        print("--out of user profile")
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
#         button.takeScreenShort(os.path.basename(__file__))
        adbCmd.stopApp("mobi.hubbler.app")
        resp.append(False)
        resp.append(printMsg.printException(e,os.path.basename(__file__)))
    return resp

if __name__=="__main__":
    action()