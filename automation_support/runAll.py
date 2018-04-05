import os
# from automation_support import printMsg, adbCmd,TClogIn,setUp
from automation_support import *
def allRun(test):
    try:
            count = 0
            fail = 0
            failResp = []
            passResp = []
            status = []

            for v in test:
                    adbCmd.launchApp("mobi.hubbler.app", "StartActivity")
                    status = v.action()
                    count = count+1
                    if status[0] == False:
                        fail = fail+1;
                        failResp.append(status[1])
                        adbCmd.stopApp("mobi.hubbler.app") 
                    else :
                        passResp.append(status[1])
#                         adbCmd.stopApp("mobi.hubbler.app") 
    except Exception as e:
            printMsg.printException(e,os.path.basename(__file__))
            pass
    return [fail,count,failResp,passResp]