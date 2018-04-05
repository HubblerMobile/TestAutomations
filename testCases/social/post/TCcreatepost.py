from automation_support import button, adbCmd, printMsg, setUp,\
    variables
from automation_support import TClogIn
import os
from time import sleep
def action():
    resp = []
    try:
        button.createPost().click()
        button.enterText(txt=variables.post['single_line_text'])
        button.post().click()
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
        sleep(1);
    except Exception as e:
        button.takeScreenShort(os.path.basename(__file__))
        resp.append(False)
        resp.append(printMsg.printException(e,os.path.basename(__file__)))
    return resp

if __name__=="__main__":
    adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
    action()