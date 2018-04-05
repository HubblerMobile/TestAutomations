import os 
import clickScrollTestCases
import time
import datetime
from automation_support import adbCmd
from clickScrollTestCases import userProfile,user_group_channel_search,channel,group,message
# for root, dirs, files in os.walk("clickScrollTestCases"):
#     print(files)
#     for filename in files:
# #         print(filename)
#         if filename[-3: ] == '.py':
#             if filename == "__init__.py":
#                 continue 
#             print()
# #             os.system('python {}'.format(filename))
#         else:
#             continue
if __name__=="__main__":
    adbCmd.stopApp("mobi.hubbler.app")
    curr = datetime.datetime.now()
    print("start time ",curr.strftime("%Y-%m-%d %H:%M:%S"))
    print("started")
#     userProfile.action()
    channel.action()
    group.action()
    user_group_channel_search.action()
    message.action()
#     group.action()
    print("stopped")
    curr = datetime.datetime.now()
    print("start time ",curr.strftime("%Y-%m-%d %H:%M:%S"))
    
    