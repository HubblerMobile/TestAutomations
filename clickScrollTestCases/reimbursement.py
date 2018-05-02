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
        button.findText("Apps").click()
        print("-------reimbursement--------")
        print("--apps are loading successfully")
        button.findTextContain('Reimbursement').click()
        print ("--reimbursment app clicked to open")
        time.sleep(1)
        button.deviceBack()
        print("--device back button is clicked in reimbursment app")
        button.findTextContain('Reimbursement').click()
        button.backReimbursementLandingPage().click()
        print("--app back button clicked in reimbursment landing page")
        button.findTextContain('Reimbursement').click()
        button.listView().fling.toBeginning()
        print("--pulled to refresh in self view")
        button.listView().child()[0].click()
        print("--self claim report opened")
        button.backReimbursementLandingPage().click()
        print("--app back button clicked in self claim trail")
        button.listView().child()[0].click()
        button.listView().child()[0].click()
        print("--self claims cards page opened")
        button.backReimbursementLandingPage().click()
        print("--app back button is clicked in self claim's cards page")
        button.listView().child()[0].click()
        # button.listView().child()[0].click()
        button.findTextContain("02 May 2018  ").click()
        "three back clickes to come to reimbursement landing page"
        button.backReimbursementLandingPage().click()
        print("--app back button clicked in individual card's page")
        button.backReimbursementLandingPage().click()
        button.backReimbursementLandingPage().click()
        button.filterReimbursment().click()
        print("--filter in self view opened")
        button.backReimbursementLandingPage().click()
        print("--app back button is clicked in self reimbursment filter")
        button.filterReimbursment().click()
        button.findTextContain("Pending").click()
        button.findTextContain("APPLY").click()
        button.findTextContain("Inbox").click()
        print("--team inbox opened")
        button.listView().child()[0].click()
        print("--subordinate's claim opened")
        button.findTextContain("Nikesh").click()
        print("--subordinate's profile opened from his claim report")
        time.sleep(1)
        button.deviceBack()
        print("--device back button clicked in subordinate profile")
        button.findTextContain("02 May 2018  ").click()
        print("--card from subordinate's claim is opened")
        button.backReimbursementLandingPage().click()
        button.backReimbursementLandingPage().click()
        button.filterReimbursment().click()
        button.findTextContain("Rejected").click()
        button.findTextContain("APPLY").click()


        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
        #         button.takeScreenShort(os.path.basename(__file__))
        resp.append(False)
        resp.append(printMsg.printException(e, os.path.basename(__file__)))
    return resp


if __name__ == "__main__":
    action()
