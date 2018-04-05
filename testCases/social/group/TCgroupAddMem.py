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
        button.group().click()
        button.enterText(variables.group['groupNm'])
        time.sleep(s)
        button.openGrp(ind=0).click()
        button.openGrpDtl().click()
        button.addGrpMem2().click()
        button.enterText(variables.group['groupNewMem'])
        time.sleep(s)
        button.selectGrpMem().click()
        button.addGrpMem().click()
        time.sleep(s)
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
        button.takeScreenShort(os.path.basename(__file__))
        resp.append(False)
        resp.append(printMsg.printException(e,os.path.basename(__file__)))
    return resp

if __name__=="__main__":
    action()