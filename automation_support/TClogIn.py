from automation_support import button, variables, printMsg,adbCmd
import time
import os


def action(number=None):
    s = variables.s
    resp =[]
    try:
        try:
            button.contin().click()
        except Exception as e:
            resp.append(True)
            resp.append(printMsg.printSuccess(os.path.basename(__file__)))
            return resp
        d = button.d
        time.sleep(s)
        "provide access to read contact"
        try:
            button.findText("ALLOW").click()
        except Exception as e:
            pass
        button.countryCode().click()
        button.searchCountryCode().click()
        button.enterText(txt="india")
        button.findText("+91").click()
        if not number:
            number =variables.user['user1_number']
        button.enterText(txt=number)
        button.contin().click()
        d(resourceId="mobi.hubbler.app:id/otp1").set_text('1')
        d(resourceId="mobi.hubbler.app:id/otp2").set_text('2')
        d(resourceId="mobi.hubbler.app:id/otp3").set_text('2')
        d(resourceId="mobi.hubbler.app:id/otp4").set_text('2')
        d(resourceId="mobi.hubbler.app:id/otp5").set_text('2')
        d(resourceId="mobi.hubbler.app:id/otp6").set_text('1')
        time.sleep(5)
        button.hubbler2Account().click()
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
        time.sleep(5)
    except Exception as e:
        button.takeScreenShort(os.path.basename(__file__))
        resp.append(False)
        resp.append(printMsg.printException(e,os.path.basename(__file__)))
    return resp

if __name__=="main":
    adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
    action()