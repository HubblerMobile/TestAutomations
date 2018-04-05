from automation_support import button, adbCmd, printMsg, setUp,\
    variables
from automation_support import TClogIn
import os
import time
from localUiautomator.uiautomator import device

def action():
    s= variables.s
    
    resp = []
    try:
        adbCmd.stopApp("mobi.hubbler.app")
        adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
        "MsgMessanger open close"
        button.MsgMessanger().click()
        print("--message opens successfully")
        time.sleep(1)
        button.deviceBack()
        print("--device back button works successfully in chats page")
        button.MsgMessanger().click()
        button.MsgBackButton().click()
        print("--app back button works successfully in chats page")
        print("MsgMessanger open close successful")
        "end MsgMessanger open close"
        "open chat "
        button.MsgMessanger().click()
        time.sleep(5)
        button.MsgOpenChat(chatIndex=0).click()
        print("--chat opens successfully")
        time.sleep(1)
        button.deviceBack()
        print("--device back button works successfully in chat page")
        time.sleep(1)
        button.MsgOpenChat(chatIndex=0).click()
        button.MsgBackButton().click()
        print("--app back button works")
        print("Messanger chat successful")
        "end open chat"
        "chat screen activity"
        button.MsgOpenChat(chatIndex=0).click()
        time.sleep(1)
        button.MsgChatHeader().click()
        time.sleep(1)
        button.deviceBack()
        time.sleep(1)
        button.MsgSendIcon().click()
        time.sleep(1)
        button.MsgChatScreen().scroll.vert.backward(steps=100)
        button.MsgChatScreen().scroll.vert.forward(steps=10)
        button.MsgBackButton().click()
        print("MsgMessanger chat screen activity successful")
        "end chat screen activity"
        "MsgMessanger search activity"
        button.MsgSearchIcon().click()
        time.sleep(1)
        button.deviceBack()
        button.deviceBack()
        button.MsgSearchIcon().click()
        button.MsgBackButton().click()
        button.MsgSearchIcon().click()
        time.sleep(5)
        button.MsgOpenChatFromSearch().click()
        print("MsgMessanger search activity successful")
        "end MsgMessanger search activity"
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
#         button.takeScreenShort(os.path.basename(__file__))
        adbCmd.stopApp("mobi.hubbler.app")
        resp.append(False)
        resp.append(printMsg.printException(e,os.path.basename(__file__)))
    return resp

if __name__=="__main__":
    action()