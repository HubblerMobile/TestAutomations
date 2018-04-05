import unittest
import os
import subprocess
from uiautomator import Adb
from automationTest.automation_support import adbCmd



class gh(unittest.TestCase):
    def __init__(self):
        self.do()
    def do(self):
        emulators = Adb().devices()
        for emu in emulators:
            print(emu)
            v=emu.split("-")[1]
            print(v)
        
        
if __name__=="__main__":
    gh()
    
    