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

        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
        #         button.takeScreenShort(os.path.basename(__file__))
        resp.append(False)
        resp.append(printMsg.printException(e, os.path.basename(__file__)))
    return resp


if __name__ == "__main__":
    action()
