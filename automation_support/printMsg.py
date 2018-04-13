import inspect, os
import sys
import time

def printException(e,file):
    try:
        exc_type, exc_obj,tb = sys.exc_info()
        lineno = tb.tb_lineno
#         if e.message:
#             print("file :",'"'+os.path.abspath(file)+':"',lineno,"exception class :",e.__class__.__name__,"exception :",e.message)
#         else:
#             print("file :",'"'+os.path.abspath(file)+':"',lineno,"exception class :",e.__class__.__name__,"exception :",e)
        print("file :",'"'+os.path.abspath(file)+':"',lineno,"exception class :",e.__class__.__name__,"exception :",e)
        return "file :",'"'+file+':"',"line :",lineno,"exception class :",e.__class__.__name__,"exception :",e
#         return "file :",'"'+os.path.abspath(file)+':"',lineno,"exception class :",e.__class__.__name__,"exception :",e
    except Exception as e:
        print(e)

def printSuccess(file):
#     exc_type, exc_obj,tb = sys.exc_info()
#     lineno = tb.tb_lineno
    print("file :"+os.path.abspath(file)+": Success")
    return "file :"+file+": Success"
#     return "file :"+os.path.abspath(file)+": Success"


 