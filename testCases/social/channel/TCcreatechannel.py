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
        button.createCnl().click()
        button.enterCnlnm(variables.channel['channelNm'], clear = True)
#         button.backSys()
        button.enterCnlTg(variables.channel['channelTg'], clear = True)
        print(variables.channel['channelTg'])
        button.enterCnlDs(variables.channel['channelDes'], clear = True)
        button.backSys()
        button.enterCnlCt().click()
        button.selectCnlCt(variables.channel['channelCt']).click()
        button.createCnlDn().click()

        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
        button.takeScreenShort(os.path.basename(__file__))
        resp.append(False)
        resp.append(printMsg.printException(e,os.path.basename(__file__)))
    return resp

if __name__=="__main__":
    action()