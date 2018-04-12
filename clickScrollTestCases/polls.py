from automation_support import button, adbCmd, printMsg, setUp, \
    variables
from automation_support import TClogIn
import os
import time
from localUiautomator.uiautomator import device


def action():
    s = variables.s

    resp = []
    try:
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("\n\n")
        button.menu().click()
        button.findText("Polls").click()
        print("--polls page opened successfully")
        time.sleep(5)
        button.deviceBack()
        print("--device back button is working successfully in polls page")
        button.menu().click()
        button.findText("Polls").click()
        button.backPollAllPages().click()
        print("--app back button is working successfully in polls page")
        button.menu().click()
        button.findText("Polls").click()
        button.listView().scroll.vert.forward(steps=10)
        button.listView().scroll.vert.backward(steps=10)
        button.listView().scroll.vert.backward(steps=10)
        print("--scroll works successfully in polls page")
        button.listView().child()[0].click()
        print("--poll is opening successfully")
        time.sleep(1)
        button.deviceBack()
        print("--device back button is working successfully in poll's page")
        button.listView().child()[0].click()
        button.backPollAllPages().click()
        print("--app back button is working successfully")
        button.listView().child()[0].click()
        button.findText("Invite").click()
        print("--invite page is opening successfully")
        time.sleep(1)
        button.deviceBack()
        button.findText("Invite").click()
        button.backPollAllPages().click()
        print("--app back button is working successfully in invite page")
        button.findText("Invite").click()
        button.listView().scroll.vert.forward(steps=10)
        button.listView().scroll.vert.backward(steps=10)
        print("--scroll is working successfully in invite page")
        button.enterText("vig")
        time.sleep(1)
        button.findText("Vignes K")
        print("--search is working successfully in invite page")
        button.backPollAllPages()
        button.findText("Invite").click()
        print("--user's profile is openign successfully form invite page")
        button.findText("Invite").click()
        button.backPollAllPages().click()
        button.findText("Vote details").click()
        print("--poll details page opened successfully")
        time.sleep(1)
        button.deviceBack()
        button.deviceBack()
        print("--device back button  is working successfully in poll details page")
        button.findText("Vote details").click()
        button.backPollAllPages().click()
        print("--app back button is working successfully in poll details page")
        button.findText("Vote details").click()
        button.findText("Yet to vote (2)").sibling().click()
        print("--yet to vote tab is openign successfully")
        button.findText("Invited (2)").sibling().click()
        print("--Invited tab is openign successfully")
        button.findText("Voted (1)").sibling().click()
        print("--Voted tab is openign successfully")
        button.enterText("manish")
        time.sleep(1)
        print("--search is working successfully in poll details page")
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
        #         button.takeScreenShort(os.path.basename(__file__))
        adbCmd.stopApp("mobi.hubbler.app")
        resp.append(False)
        resp.append(printMsg.printException(e, os.path.basename(__file__)))
    return resp


if __name__ == "__main__":
    action()