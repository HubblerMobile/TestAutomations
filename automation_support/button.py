from localUiautomator.uiautomator import *
import time
import os
from automation_support import variables, printMsg

# d=Device('emulator-5554')
d = device
arr = []
"general"
def scrollView():
    return d(className="android.widget.ScrollView")
def back():
    return d(className="android.widget.ImageButton")
def recycleView():
    return d(className="android.support.v7.widget.RecyclerView")

def findTextContain(txt):
    return d(textContains=txt)
def listView():
    return d(className="android.widget.ListView")


def unlockScreen():
    d.swipe().unlock()


def feed():
    return d(resourceId="mobi.hubbler.app:id/feedsList")


def getAllEle():
    return d(packageName="mobi.hubbler.app")


def dump():
    print(d.dump())


def goToLandingPage():
    run = True
    count = 0
    while run:
        print(count)
        count += 1;
        try:
            print(findText("Presslvvj h"))
            findText("Presskjbib")
            run = False
        except Exception as e:
            pass


def enterText(txt=None, clear=None):
    txtField = d(className='android.widget.EditText')
    if clear:
        txtField.clear_text()
    if txt:
        txtField.set_text(txt)


def clearSearchTxt():
    return d(resourceId="mobi.hubbler.app:id/ivClose")


def popupCancel():
    return d(resourceId='mobi.hubbler.app:id/tvCancel', text='Cancel')


def appBack():
    return d(resourceId='mobi.hubbler.app:id/ivBackButton')


def deviceBack():
    d.press.back()


def backSys():
    d.press.back()


def takeScreenShort(self, file=None):
    try:
        if not file:
            file = 'screenshot' + time.strftime("%H_%M_%S") + '.png'
        else:
            file = file + time.strftime("%H_%M_%S") + '.png'
        directory = os.path.dirname(
            os.path.dirname(os.path.dirname(__file__))) + "/output/output_screen/" + time.strftime("%d_%m_%Y") + "/"
        #         for windows only
        #         directory.replace('\\','/')
        if not os.path.exists(directory):
            os.makedirs(directory)
        print(device.screenshot(directory + file))
        #         device.sc
        print(file)
        print(directory)

    except Exception as e:
        printMsg.printException(e, os.path.basename(__file__))


"end general"
"login action"


def contin():
    return d(resourceId="mobi.hubbler.app:id/continueButton")


def logOut():
    return d(resourceId='mobi.hubbler.app:id/design_menu_item_text', text='Logout')


def logoutDn():
    return d(resourceId='mobi.hubbler.app:id/tvDone', text='Logout')


def hubbler2Account():
    return d(text="hubbler 2")


"end login actions"

"channel buttons"


def channelFollower():
    return d(resourceId='mobi.hubbler.app:id/container')


def channelFollowers():
    return d(resourceId='mobi.hubbler.app:id/tvFollowers', text='followers')


def channelMemRem():
    return d(resourceId='android:id/title', text='Remove')


def addCnlSelMem():
    return d(resourceId='mobi.hubbler.app:id/btCreate', text='Add')


def selectChnlMem():
    return d(resourceId='mobi.hubbler.app:id/parent')


def channelEdit():
    return d(resourceId='mobi.hubbler.app:id/tvSettings', text='Edit')


def channelFolCount():
    return d(resourceId='mobi.hubbler.app:id/tvFollowersCount').text


def inviteCnlMemDn():
    return d(resourceId='mobi.hubbler.app:id/btCreate', text='Invite')


def selectCnlMem(ind):
    return d(resourceId='mobi.hubbler.app:id/parent')


def inviteCnlMem():
    return d(resourceId='mobi.hubbler.app:id/reachout')


def editCnlUpdt(ind):
    return d(resourceId='mobi.hubbler.app:id/btCreate')


def openCnl(ind):
    return d(className='android.widget.RelativeLayout', instance=ind)


def backCnlCrt():
    return d(resourceId='mobi.hubbler.app:id/imageView1')


def createCnlDn():
    return d(resourceId='mobi.hubbler.app:id/btCreate', text='Create')


def selectCnlCt(txt):
    return d(resourceId='mobi.hubbler.app:id/name', text=txt)


def enterCnlCt():
    return d(resourceId='mobi.hubbler.app:id/categorySection')


def enterCnlDs(ds, clear=None):
    txtField = d(resourceId='mobi.hubbler.app:id/etDescription')
    if clear:
        txtField.clear_text()
    txtField.set_text(ds)


def enterCnlTg(tg, clear=None):
    txtField = d(resourceId='mobi.hubbler.app:id/etTag')
    if clear:
        txtField.clear_text()
    txtField.set_text(tg)


def enterCnlnm(nm, clear=None):
    txtField = d(resourceId='mobi.hubbler.app:id/etChannel')
    if clear:
        txtField.clear_text()
    txtField.set_text(nm)


def txfield(txtField, txt, clear):
    if clear:
        txtField.clear_text()
    txtField.set_text(txt)


def backCnl():
    return d(resourceId='mobi.hubbler.app:id/ivBackButton')


def createCnl():
    return d(resourceId='mobi.hubbler.app:id/plusButtun', text='Create')


def channel():
    return d(resourceId='mobi.hubbler.app:id/design_menu_item_text', text='Channels')


def org():
    return d(resourceId='mobi.hubbler.app:id/rbOrg', text='Organization')


def openChannel(ind):
    return d(className='android.widget.ListView').child(className='android.widget.RelativeLayout', instance=ind)


def channelList():
    return d(resourceId="mobi.hubbler.app:id/listView1")


def channelDP():
    return d(resourceId="mobi.hubbler.app:id/profilePic")


def channelCoverPic():
    return d(resourceId="mobi.hubbler.app:id/ivCoverPic")


def channelListSearchClear():
    return d(resourceId="mobi.hubbler.app:id/ivClose")


def channelToInviteList():
    return d(resourceId="mobi.hubbler.app:id/listView1")


"end channel buttons"

"group buttons"


def exitGrpDn():
    return d(resourceId='mobi.hubbler.app:id/tvDone', text='Exit')


def removeGrpMeOpt():
    return d(resourceId='android:id/title', text='Remove')


def mkadminGrpOpt():
    return d(resourceId='android:id/title', text='Make group admin')


def updateGrpNmEd():
    return d(resourceId='mobi.hubbler.app:id/btCreate', text='Update')


def backGrpNmEd():
    return d(resourceId='mobi.hubbler.app:id/backBtn')


def exitGrp():
    return d(resourceId='mobi.hubbler.app:id/exitSection')


def grpMem(ind):
    return d(resourceId='mobi.hubbler.app:id/membersList').child(className='android.widget.LinearLayout', instance=ind)


def addGrpMem2():
    return d(resourceId='mobi.hubbler.app:id/addMember', text='Add members')


def editGrpNm():
    return d(resourceId='mobi.hubbler.app:id/editProfile')


def openGrpDtl():
    return d(resourceId='mobi.hubbler.app:id/titleSection')


def openGrp(ind):
    return d(className='android.widget.ListView').child(className='android.widget.LinearLayout', instance=ind)


def addGrpMem():
    return d(resourceId='mobi.hubbler.app:id/btCreate', text='Add')


def selectGrpMem():
    return d(resourceId='mobi.hubbler.app:id/parent')


def backGrpAddmem():
    return d(resourceId='mobi.hubbler.app:id/imageView1')


def backGrpCr():
    return d(resourceId='mobi.hubbler.app:id/back_button')


def nexttGrp():
    return d(resourceId='mobi.hubbler.app:id/btCreate', text='Next')


def chooseGrpPic():
    return d(resourceId='mobi.hubbler.app:id/profilePic')


def createGrp():
    return d(resourceId='mobi.hubbler.app:id/plusButtun', text='Create')


def group():
    return d(resourceId='mobi.hubbler.app:id/design_menu_item_text', text='Groups')


def groupList():
    return d(resourceId="mobi.hubbler.app:id/listView1")


def backGroupPage():
    return d(resourceId='mobi.hubbler.app:id/back_button')


def openGroupDetails():
    return d(resourceId='mobi.hubbler.app:id/titleSection')


def backGroupDetailsPage():
    return backGroupPage()


def openGroupDp():
    return chooseGrpPic()


def groupMemberList():
    return d(resourceId="mobi.hubbler.app:id/membersList")


def backGroupAddMember():
    return d(resourceId='mobi.hubbler.app:id/imageView1')


"end group buttons"

"top buttons"


def menu():
    return d(resourceId='mobi.hubbler.app:id/menuIcon')


def search():
    return d(resourceId='mobi.hubbler.app:id/searchButton')


def message():
    return d(resourceId='mobi.hubbler.app:id/message_btn')


def notification():
    return d(resourceId='mobi.hubbler.app:id/notificationIcon')


def Activity():
    return d(resourceId='mobi.hubbler.app:id/feedButton', text='Activity')


def Apps():
    return d(resourceId='mobi.hubbler.app:id/apps', text='Apps')


"end top buttons"

"post buttons/methods"


def cancelPostDel():
    return d(resourceId='mobi.hubbler.app:id/tvCancel', text='Cancel')


def deletePost():
    return d(resourceId='mobi.hubbler.app:id/tvDone', text='Delete')


def enablePostOpt():
    return d(resourceId='android:id/title', text='Enable')


def disablePostOpt():
    return d(resourceId='android:id/title', text='Disable')


def deletePostOpt():
    return d(resourceId='android:id/title', text='Delete')


def postComment():
    return d(resourceId='mobi.hubbler.app:id/sendButton')


def commentCount():
    return d(resourceId='mobi.hubbler.app:id/commentCount').text


def comment():
    return d(resourceId='mobi.hubbler.app:id/commentSection')


def backPost():
    return d(resourceId='mobi.hubbler.app:id/ivBackButton')


def findText(tex):
    return d(text=tex)


def likeCount():
    return d(resourceId='mobi.hubbler.app:id/likeCount').text


def like():
    return d(resourceId='mobi.hubbler.app:id/ivLike')


def createPost():
    return d(resourceId="mobi.hubbler.app:id/fab_btn")


def post():
    return d(text="Post")


"end post buttons/methods"

"user_group_channel_search"


def popupUnfollow():
    return d(resourceId="mobi.hubbler.app:id/tvDone", text="Unfollow")


def userTab():
    return d(resourceId="mobi.hubbler.app:id/tab").child().child(text="Users")


def userTab2():
    return d(text="Users")


def channelTab():
    return d(text="Channels")


def groupTab():
    return d(text="Groups")


def UCGuserFollow():
    return d(resourceId="mobi.hubbler.app:id/invite");


def UCGuserOpen():
    return d(resourceId="mobi.hubbler.app:id/globalListView").child()[0]


# .sibling(resourceId="mobi.hubbler.app:id/invite")
"end user_group_channel_search"
"user profile"


def userProfileBack():
    return d(resourceId="mobi.hubbler.app:id/primaryBack")


"end user profile"
"message"


def MsgBackButton():
    return d(className="android.widget.ImageButton")


def MsgMessanger():
    return d(resourceId="mobi.hubbler.app:id/message_btn")


def MsgSearchIcon():
    return d(resourceId="mobi.hubbler.app:id/action_search")


def MsgOpenChat(chatIndex):
    return d(resourceId="mobi.hubbler.app:id/inbox_list").child()[0]


def MsgOpenChatFromSearch():
    return d(resourceId="mobi.hubbler.app:id/user_list").child()[0]


def MsgChatHeader():
    return d(resourceId="mobi.hubbler.app:id/header_author_block")


def MsgSendIcon():
    return d(resourceId="mobi.hubbler.app:id/send_btn")


def MsgChatScreen():
    return d(resourceId="mobi.hubbler.app:id/conversation_list")


"end message"
"user profile"


def drawerHeader():
    return d(resourceId="mobi.hubbler.app:id/headerMainBlock")


def userProfilePage():
    return d(resourceId="mobi.hubbler.app:id/feedsList")


def following():
    return d(resourceId="mobi.hubbler.app:id/tvFollowing")


def followers():
    return d(resourceId="mobi.hubbler.app:id/tvFollowers")


def followingCount():
    return d(resourceId="mobi.hubbler.app:id/tvFollowingCount")


def followersCount():
    return d(resourceId="mobi.hubbler.app:id/tvFollowersCount")


def mobileOnProfile():
    return d(resourceId="mobi.hubbler.app:id/tvMob")


def emailOnProfile():
    return d(resourceId="mobi.hubbler.app:id/tvEmail")


def backUserProfile():
    return d(resourceId="mobi.hubbler.app:id/primaryBack")


def follower_followingUser():
    return d(resourceId="mobi.hubbler.app:id/listView").child()[0]


def follower_followingList():
    return d(resourceId="mobi.hubbler.app:id/listView")


"end user profile"
"events"
def activeEvent():
    return d(resourceId="mobi.hubbler.app:id/tvUpcoming")
def pastEvent():
    return d(resourceId="mobi.hubbler.app:id/tvPast")
def backEventsPage():
    return d(resourceId="mobi.hubbler.app:id/backBtn1")
def active_pastEvent():
    return d(resourceId="mobi.hubbler.app:id/titleSection")
def backEventDetailsPage():
    return d(resourceId="mobi.hubbler.app:id/imageView1")
def optionsOnEvent():
    return d(resourceId="mobi.hubbler.app:id/item_going1")
def invitePeople():
    return d(resourceId="mobi.hubbler.app:id/invite_people_section")
def backInvitePeoplePage():
    return d(resourceId="mobi.hubbler.app:id/imageView1")
def eventLocation():
    return d(resourceId="mobi.hubbler.app:id/eventLocation")
def backEventLocationPage():
    return d(resourceId="mobi.hubbler.app:id/imageView1")
def eventStatusGoingPeopleList():
    return d(resourceId="mobi.hubbler.app:id/item_going")
def eventStatusMaybePeopleList():
    return d(resourceId="mobi.hubbler.app:id/item_maybe")
def invitedPeopleList():
    return d(resourceId="mobi.hubbler.app:id/item_invite")
def backEventStatusPeopleList():
    return d(resourceId="mobi.hubbler.app:id/ivBackButton")
def eventCoverPicture():
    return d(resourceId="mobi.hubbler.app:id/eventCoverImage")
"end events"

"poll"
def inviteButton():
    return d(resourceId="mobi.hubbler.app:id/action_done")
def voteDetails():
    return  d(resourceId="mobi.hubbler.app:id/voteDetails")
def backPollInvitPage():
    return d(className="android.widget.ImageButton")
def backPollDetailsPage():
    return d(className="android.widget.ImageButton")
def backPollAllPages():
    return d(className="android.widget.ImageView")[0]
"end poll"

"end post"
def like():
    return d(resourceId="mobi.hubbler.app:id/ivLike")
def likeList():
    return d(resourceId="mobi.hubbler.app:id/tvLike")
def comment():
    return d(resourceId="mobi.hubbler.app:id/commentLayout")
def post():
    return d(resourceId="mobi.hubbler.app:id/content_section")
def postActionOption():
    return  d(resourceId="mobi.hubbler.app:id/overflow_menu")
def postUser():
    return  d(resourceId="mobi.hubbler.app:id/head_section")
def postGroup():
    return d(resourceId="mobi.hubbler.app:id/header")
def backPostPage():
    return  d(resourceId="mobi.hubbler.app:id/ivBackButton")
"post"

"attendance"
def selfHistory():
    return d(resourceId="mobi.hubbler.app:id/action_history")
def teamHistory():
    return d(resourceId="mobi.hubbler.app:id/action_inbox")
def previousDate():
    return d(resourceId="mobi.hubbler.app:id/prev_btn")
def nextDate():
    return d(resourceId="mobi.hubbler.app:id/next_btn")
def locationFilter():
    return d(resourceId="mobi.hubbler.app:id/action_filter")
def callMessageOption():
    return d(resourceId="mobi.hubbler.app:id/overflow_menu")
def userHeader():
    return d(resourceId="mobi.hubbler.app:id/header_author_block")
def backAttendance():
    return d(className="android.widget.ImageButton")[0]
def attendanceApp():
    return d(textContains="Attendance")
"end attendance"

"leave"
def leaveFilter():
    return d(resourceId="mobi.hubbler.app:id/action_filter")
def teamViewLeave():
    return d(resourceId="mobi.hubbler.app:id/action_manager")
def leaveTeamViewSearch():
    return d(resourceId="mobi.hubbler.app:id/search_button")
def leaveTeamViewSearchClear():
    return d(resourceId="mobi.hubbler.app:id/search_close_btn")
def leaveDetailsUserHeader():
    return d(resourceId="mobi.hubbler.app:id/profileLayout")
def backLeaveDetaislPage():
    return d(resourceId="mobi.hubbler.app:id/imageView1")
"end leave"