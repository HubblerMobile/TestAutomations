from automation_support import button, adbCmd, printMsg, setUp,\
    variables
from automation_support import TClogIn
import os
import time
# from asyncio.tasks import wait
def action():
    s=variables.s
    resp = []
    try:
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        "back code"
        print("\n\n")
        print("-------main search--------")
        button.search().click()
        print("--user_channel_group search opens successfully")
        button.appBack().click()
        print("--app back button works successfully in user_channel_group page")
        button.search().click()
        time.sleep(1)
        button.deviceBack()
        button.deviceBack()
        print("--device back button works successfully in user_channel_group page")
        "end back code"
        "tab switching code"
        button.search().click()
        button.channelTab().click()
        button.channelTab().click()
        print("--channel tab click successful")
        button.groupTab().click()
        button.groupTab().click()
        print("--group tab click successful")
        button.userTab().click()
        button.userTab().click()
        print("--user tab click successful")
        "tab switching code"
        "open user profile code"
        button.UCGuserOpen().click()
        print("--user profile opens successfully form users tab")
        time.sleep(1)
        button.deviceBack()
        "end open user profile code"
        "search user"
        button.enterText("Admin Account")
        print("--search is successful in user_group_channel")
        time.sleep(1)
        button.clearSearchTxt().click()
        "end search user"
        "open channel"
        button.channelTab().click()
        button.UCGuserOpen().click()
        print("--channel opens successfully")
        time.sleep(1)
        button.deviceBack()
        "end open channel"
        "open group"
        button.groupTab().click()
        button.UCGuserOpen().click()
        print("--group opens successfully")
        time.sleep(1)
        button.deviceBack()
        "end open group"
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
#         button.takeScreenShort(os.path.basename(__file__))
        adbCmd.stopApp("mobi.hubbler.app")
        resp.append(False)
        resp.append(printMsg.printException(e,os.path.basename(__file__)))
    return resp

if __name__=="__main__":
    print(time.time())
    action()
    # print(time.time())