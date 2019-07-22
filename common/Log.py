#coding:utf-8
#__author:"July"
#__date:2019\6\25 0025

import logging
import  threading
from datetime import datetime
import  readConfig
import os

class Log:
    def __init__(self):
        global logPath,resultPaht,proDir
        proDir=readConfig.proDir
        resultPaht=os.path.join(proDir,"result")
        if not os.path.exists(resultPaht):
            os.mkdir(resultPaht)
        logPath=os.path.join(resultPaht,str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        #定义logger
        self.logger=logging.getLogger()
        #定义logger登记
        self.logger.setLevel(logging.INFO)
        #定义handler
        handler=logging.FileHandler(os.path.join(logPath,"output.log"))
        #设置输出格式
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

class MyLog:
    log=None
    mutex=threading.Lock()

    def __init__(self):
        pass


    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log=Log()
            MyLog.mutex.release()

        return MyLog.log



