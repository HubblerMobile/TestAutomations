import time
import os
print(os.getcwd())
# import webApp
from automationTest.automation_support import button, adbCmd, printMsg, setUp
from automationTest.automation_support import TClogIn

from automationTest.automation_support import TClogIn
from automationTest.testCases.social.post import TCcreatepost
from automationTest.automation_support.testSelector import testSelector
from automationTest.automation_support.runAll import allRun
from automationTest.automation_support.testCases import testCases
from automationTest.testCases.social.group import TCcreateGroup,\
    TCeditGroup, TCgroupAddMem, TCgroupRmMem
# from androidAutomation.webApp.automationTest.testCases.social.group import TCcreateGroup

# response = []
test = [];
groupTest = []
groupTest.append(TClogIn)
# groupTest.extend((TClogIn))
def setTest(testArray):
    test = testArray

def run(mod):
    setU()
    resp = body(mod)
    return resp
def setU():
    "do setup"
    setUp.setUp()
def body(mod):
    start_time =time.time()
    time.sleep(10)
    test = []
    test = testCases(mod)
    response = allRun(test)
    adbCmd.stopApp("mobi.hubbler.app")
    print('total fail :', response[0])
    print('total success :',response[1] - response[0])
    print('total run :',response[1])
    print("--- %s seconds ---" %round(time.time() - start_time,2))
    return response   

if __name__=='__main__':
    s = run("group")
    print(s)
    