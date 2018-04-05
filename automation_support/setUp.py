# from automationTest.automation_support import adbCmd
from automation_support import  *
import os
def setUp():
#     app = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),'media/app-debug.apk')
#     adbCmd.installApp(app)
    adbCmd.launchApp("mobi.hubbler.app", "StartActivity")