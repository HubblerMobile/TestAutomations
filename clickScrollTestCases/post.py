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
        print("\n\n")
        print("------post--------")
        button.like().click()
        print("--Post liked successfully")
        button.likeList().click()
        print("--Post likelist opened successfully")
        time.sleep(1)
        button.deviceBack()
        print("--device back button is working in like list successfully")
        button.likeList().click()
        button.appBack().click()
        print("--app back button is working in like list successfully")
        button.like().click()
        print("--post unliked successfully")
        button.comment().click()
        print("--comment opened successfully")
        time.sleep(1)
        button.deviceBack()
        print("--device back button is working successfully in comments page")
        button.comment().click()
        button.appBack().click()
        print("--app back button is working successfully in comments page")
        button.postActionOption().click()
        print("--post action options list opened successfully")
        button.findText("Disable").click()
        print("--post disabled successfully")
        button.postActionOption().click()
        button.findText("Enable").click()
        print("--post enabled successfully")
        button.post().click()
        print("--post oponed successfully")
        time.sleep(1)
        button.deviceBack()
        print("--device back button is working successfully in post page")
        button.post().click()
        button.backPostPage().click()
        print("--app back button is working successfully in post page")
        button.listView().fling.toEnd()
        print("--scrolled till end successfully")
        button.listView().fling.toBeginning()
        print("--scrolled till start successfully")
        button.listView().scroll.to(text="Text post")
        button.findText("Text post").click()
        print("--text post opened successfully")
        button.backPostPage().click()
        button.listView().scroll.to(text="Image")
        button.findText("Image").click()
        print("--image post opened successfully")
        button.backPostPage().click()
        # button.listView().scroll.vert.backward(steps=10)
        resp.append(True)
        resp.append(printMsg.printSuccess(os.path.basename(__file__)))
    except Exception as e:
        #         button.takeScreenShort(os.path.basename(__file__))
        resp.append(False)
        resp.append(printMsg.printException(e, os.path.basename(__file__)))
    return resp


if __name__ == "__main__":
    action()
