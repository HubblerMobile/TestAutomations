from automation_support import button, adbCmd, printMsg, setUp,\
    variables
from automation_support import TClogIn
import os
import time
def action():
    s=variables.s
    resp = []
    try:
#         adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        time.sleep(s)
        button.menu().click()
        button.channel().click()
        button.enterText(variables.channelOrg['channelNm'])
        time.sleep(s)
        button.openChannel(1).click()
        button.channelFollowers().click()
        button.enterText(variables.channelOrg['channelAddMe'])
        time.sleep(s)
        button.channelFollower().long_click()
        button.channelMemRem().click()
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
        button.takeScreenShort(os.path.basename(__file__))
        resp.append(False)
        resp.append(printMsg.printException(e,os.path.basename(__file__)))
    return resp

if __name__=="__main__":
    action()