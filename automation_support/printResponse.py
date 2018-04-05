import time

def printResp(res,start_time):
    print('total fail :', res[0])
    print('total success :',res[1] - res[0])
    print('total run :',res[1])
    print("--- %s seconds ---" %round(time.time() - start_time,2))