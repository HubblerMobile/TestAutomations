from automation_support import button, adbCmd, printMsg, setUp,\
    variables
import os
import time
s = variables.s
def action():
    resp = []
    try:
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        time.sleep(s)
        button.findText(variables.post['single_line_text']).click()
        pre = button.likeCount()
        button.like().click()
        pos = button.likeCount()
        if pos <= pre:
            raise Exception('like count same')
        button.backPost()
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
        button.takeScreenShort(os.path.basename(__file__))
        resp.append(False)
        resp.append(printMsg.printException(e,os.path.basename(__file__)))
    return resp

if __name__=="__main__":
    action()