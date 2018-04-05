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
        "open profile from drawer"
        button.menu().click()
        print("--open drawer from hamberger is fine")
        button.drawerHeader().click()
        print("--open profile from drawer is fine")
        button.userProfileBack().click()
        print("--app back button in user profile is fine")
        button.menu().click()
        button.drawerHeader().click()
        time.sleep(2)
        button.deviceBack()
        print("--device back button in user profile is fine")
        "end open profile from drawer"
        "following section"
        button.menu().click()
        button.drawerHeader().click()
        button.following().click()
        print("--following page opened successfully")
        button.appBack().click()
        print("--app back button in following page is fine")
        button.following().click()
        time.sleep(2)
        button.deviceBack()
        print("--device back button is working in following page")
        button.following().click()
        button.follower_followingList().scroll.vert.backward(steps=10)
        time.sleep(2)
        button.follower_followingList().scroll.vert.forward(steps=10)
        print("--scroll is working in following page")
        button.enterText("Aadarsh", clear=True)
        button.clearSearchTxt().click()
        time.sleep(2)
        print("--search is working in following page")
        button.follower_followingUser().click()
        button.userProfileBack().click()
        button.appBack().click()
        button.userProfileBack().click()
        print("--user profile is opening form followers list")
        "end following section"
        "follower section"
        button.menu().click()
        button.drawerHeader().click()
        button.followers().click()
        print("--followers page is opening")
        button.appBack().click()
        print("--app back button is working in follower page")
        button.followers().click()
        time.sleep(2)
        button.deviceBack()
        print("--device back button is working in follower page")
        button.followers().click()
        button.follower_followingList().scroll.vert.backward(steps=10)
        time.sleep(2)
        button.follower_followingList().scroll.vert.forward(steps=10)
        print("--scroll is working in following page")
        button.enterText("Aadarsh", clear=True)
        button.clearSearchTxt().click()
        time.sleep(2)
        print("--search is working in following page")
        button.follower_followingUser().click()
        button.userProfileBack().click()
        button.appBack().click()
        button.userProfileBack().click()
        print("--user profile poens from following page")
        "end follower section"
        "mobile number"
        button.menu().click()
        button.drawerHeader().click()
        button.findText("1222333444").click()
        time.sleep(0.5)
        button.deviceBack()
        print("--mobile number is click-able")
        "end mobile number"
        "email"
#         button.menu().click()
#         button.drawerHeader().click()
        button.findText("manish@kumar.com").click()
        time.sleep(0.5)
        button.deviceBack()
        print("--email is click-able")
        "end email"
        "scroll in profile"
#         button.menu().click()
#         button.drawerHeader().click()
        button.userProfilePage().scroll.vert.forward(steps=10)
        button.userProfilePage().scroll.vert.backward(steps=10)
        print("--scroll is working in user profile")
        "end scroll in profile"
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