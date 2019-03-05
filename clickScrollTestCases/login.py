from automation_support import button, adbCmd, printMsg, setUp, \
    variables,TClogIn
from automation_support import TClogIn
from randomClickScroll import randomClickV3
import os
import time
from localUiautomator.uiautomator import device



if __name__ == "__main__":
    adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
    TClogIn.action()
