import os
import subprocess
appPackage = "mobi.hubbler.app"
appActivity = "mobi.hubbler.app.StartActivity"

# 
emulator = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),'automation_sdk/tools/emulator ')
if "ANDROID_HOME" in os.environ:
                filename = "adb.exe" if os.name == 'nt' else "adb"
                adb = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", filename)

def allDevices():
    return os.system(adb+" devices").communicate()[0].decode("utf-8")
def launchApp(appPackag=None,appActivity=None):
    os.system(adb+" shell am start -n "+appPackag+"/"+appPackag+"."+appActivity)
    return
def stopApp(appPackage=None):
    os.system(adb+" shell am force-stop "+appPackage)
    return
def installApp(app):
    os.system(adb+" install "+app)
    return
def uninstallApp(appPackage=None):
    os.system(adb+" uninstall "+appPackage)
    return
def isAppPresent(appPackage=None):
    return os.system(adb+" shell pm list packages | grep "+appPackage)
def reInstallApp(app):
    os.system(adb+" install -r "+app)
    return
# .communicate()[0].decode("utf-8")
def runEmulator():
    w = os.system(emulator+" -avd and2 -no-window; exit;").communicate().decode("utf-8")
    print(w)
    return w
def killEmulator(device):
    print(adb +" -s "+ device +" emu kill")
    return os.system(adb +" -s "+ device +" emu kill")