from automation_support import button, adbCmd, printMsg, setUp, \
    variables
from automation_support import TClogIn
import os
import time
from localUiautomator.uiautomator import device


def action():
    s = variables.s
    arr = []
    resp = []
    try:
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        print("\n\n")
        button.menu().click()
        button.findText("Groups").click()
        print("--group list open successfully")
        button.listView().scroll.vert.forward(steps=10)
        button.listView().scroll.vert.backward(steps=10)
        print("--scroll works successfully in group list page")
        button.listView()[0].click()
        print("--group open successfully")
        time.sleep(.5)
        button.deviceBack()
        print("--device back button works successfully in group page")
        button.listView()[0].click()
        button.backGroupPage().click()
        print("--app back button works successfully in group page")
        button.listView()[0].click()
        button.listView().scroll.vert.forward(steps=10)
        button.listView().scroll.vert.backward(steps=10)
        print("--scroll works in group page successfully")
        button.openGroupDetails().click()
        print("--group details page opens successfully")
        time.sleep(1)
        button.deviceBack()
        print("--device back button works successfully in group details page")
        button.openGroupDetails().click()
        button.backGroupDetailsPage().click()
        print("--app back button works successfully in group details page")
        button.openGroupDetails().click()
        button.listView().scroll.vert.forward(steps=10)
        button.listView().scroll.vert.backward(steps=10)
        print("--scroll works in group members list")
        button.findText("Add Members").click()
        print("--add member page opens successfully in group")
        time.sleep(1)
        button.deviceBack()
        print("--device back works successfully in add member page")
        button.findText("Add Members").click()
        button.backGroupAddMember().click()
        print("--app back button works successfully in add member page")
        button.findText("Add Members").click()
        button.findText("Add").click()
        print("--add button in add member page do not crash on click")
        time.sleep(1)
        button.deviceBack()
        time.sleep(1)
        button.deviceBack()
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
        #         button.takeScreenShort(os.path.basename(__file__))
        resp.append(False)
        resp.append(printMsg.printException(e, os.path.basename(__file__)))
    return resp


if __name__ == "__main__":
    action()
