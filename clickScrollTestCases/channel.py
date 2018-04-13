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
        button.menu().click()
        print("menue opens successfully")
        button.findText("Channels").click()
        print("--channel list open successfully")
        button.openChannel(ind=1).click()
        print("--channel opens successfully")
        button.findText("followers").click()
        print("--channel follower list opens successfully")
        button.follower_followingList().scroll.vert.forward(steps=10)
        button.follower_followingList().scroll.vert.backward(steps=10)
        print("--channel followers list scrolls successfully")
        button.enterText("manish", clear=True)
        time.sleep(2)
        print("--search worked successfully")
        button.follower_followingList().child(index=0).click()
        print("--user profile opens from channel followers list successfully")
        button.userProfileBack().click()
        button.appBack().click()
        button.findText("Invite").click()
        print("--invite list is opening successfully")
        button.enterText("divya")
        time.sleep(2)
        button.channelList().child(index=0).click()
        print("--search is working in channel-to-invite list")
        button.backCnlCrt().click()
        print("--app back button is working successfully in invite list")
        button.findText("Invite").click()
        time.sleep(2)
        button.deviceBack()
        print("--device back button is working successfully in invite list")
        button.channelDP().click()
        time.sleep(2)
        button.deviceBack()
        print("--channel dp is showing-closing succesfully")
        button.channelCoverPic()
        time.sleep(2)
        button.deviceBack()
        print("--channel cover pic is showing-closing successfully")
        button.channelList().scroll.vert.forward(steps=10)
        button.channelList().scroll.vert.backward(steps=10)
        print("--channel list scrolls successfully")
        button.enterText("city 1")
        print("--search works in channel list successfully")
        time.sleep(2)
        button.channelListSearchClear().click()
        print("--channel list search clear works successfully")
        button.appBack().click()
        print("--app back button is working successfully in channel list")
        button.menu().click()
        button.findText("Channels").click()
        time.sleep(2)
        button.deviceBack()
        print("--device back button is working successfully in channel list")     
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