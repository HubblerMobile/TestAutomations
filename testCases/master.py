from automation_support import button, adbCmd, printMsg, setUp
from automation_support import TClogIn
import os
from automation_support import TClogIn
from testCases.social.post import TCcreatepost
# from automation_support.testSelector import testSelector
from automation_support.runAll import allRun
# response = []
class unitTest():
    def __init__(self):
        self.setUp()
        self.body()
    def setUp(self):
        "do setup"
        setUp.setUp()
    def body(self):
        test = []
        test.append(TClogIn)
#         test.extend((TClogIn,TCcreatepost,TCcreatepost))
        response = allRun(test)
        adbCmd.stopApp("mobi.hubbler.app")
        print('total fail :', response[0])
        print('total success :',response[1] - response[0])
        print('total run :',response[1])
       

if __name__=='__main__':
    print("runn")
    v = unitTest()
    