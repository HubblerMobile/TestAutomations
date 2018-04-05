from testCases.social.group import TCcreateGroup,\
    TCeditGroup, TCgroupAddMem, TCgroupRmMem, TCgroupExt
from automation_support import TClogIn
from testCases.social.post import TCcreatepost, TClikePost,\
    TCdeletepost, TCcommentpost
from testCases.social.channel import TCcreatechannel,\
    TCcreateorgchannel, TCchanneladdmem, TCchannelRmMem
 
def testCases(mod):
    arr = []
    "login testcase"
    arr.append(TClogIn)
    "post testcase"
    arr.extend((TCcreatepost,TClikePost,TCcommentpost,TCdeletepost))
    "group testcase"
    arr.extend((TCcreateGroup,TCeditGroup,TCgroupAddMem,TCgroupRmMem,TCgroupExt))
    "channel testcase"
    arr.extend((TCchanneladdmem,TCchannelRmMem))
    return arr

