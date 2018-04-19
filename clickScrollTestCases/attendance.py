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
        button.findText("Apps").click()
        print("--apps are loading successfully")
        print(button.findText("Attendance").sibling(className="android.widget.LinearLayout").click())
        for i in button.findText("Attendance").sibling():
            print(i.info['clickable'])
        button.findText("Attendance").sibling(className="android.widget.LinearLayout").click()
        print("--attendance is opening successfully")
        time.sleep(1)
        button.deviceBack()
        print("--device back button is working successfully in attendance")
        button.findText("Attendance").click()
        button.backAttendance().click()
        print("--app back button is working successfully in attendance")
        button.findText("Attendance").sibling().click()
        button.selfHistory().click()
        print("--self history is opening successfully")
        button.backAttendance().click()
        print("--app back button is working successfully in slef history")
        button.teamHistory().click()
        print("--self history is opening successfully in team history")
        button.backAttendance().click()
        print("--back button is working successfully in team history")
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
        #         button.takeScreenShort(os.path.basename(__file__))
        resp.append(False)
        resp.append(printMsg.printException(e, os.path.basename(__file__)))
    return resp


if __name__ == "__main__":
    action()
