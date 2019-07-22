#coding:utf-8
#__author:"July"
#__date:2019\6\26 0026

import sys
import os

AbsolutePath = os.path.abspath(__file__)#将相对路径转换成绝对路径
SuperiorCatalogue = os.path.dirname(AbsolutePath)#相对路径的上级路径
BaseDir = os.path.dirname(SuperiorCatalogue)  #在“SuperiorCatalogue”的基础上在脱掉一层路径，得到我们想要的路径。
sys.path.insert(0,BaseDir) #将我们取出来的路径加入到Python的命名空间去，并将该目录插入在第一个位置中。
import requests


from common.Log import MyLog as log
import readConfig as readConfig
from common.Log import Log
from common.configExcel import *


localReadConfig = readConfig.readConfig()

class ConfigHttp:
    def __init__(self):
        global host,port,timeout
        host = localReadConfig.get_url('baseurl')
        port = localReadConfig.get_url('port')
        timeout = localReadConfig.get_url('timeout')
        self.log=log.get_log()
        self.logger=self.log.get_logger()
        self.headers={}
        self.params={}
        self.data={}
        self.url=None
        self.files={}

    #获取URL后拼接
    def set_url(self,row,col):
        self.url = host + OperationExcel.get_cell_value(row,col)
        return self.url

    # def set_headers(self, headers):
    #     self.headers = headers
    #
    # def set_params(self,param):
    #     self.params=param

    #获取接口数据
    def set_data(self,row,col):
        data_file = OperationExcel.get_cell_value(row,col)
        print ()



    # def set_files(self,file):
    #     self.files = file

    def get(self):
        try:
            response = requests.get(self.url,headers=self.headers,data=self.data,files=self.files,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time Out!")
            return  None

    def post(self):
        try:
            response = requests.post(self.url,headers=self.headers,data=self.data,files=self.files,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time Out!")
            return  None

    def put(self):
        try:
            response = requests.put(self.url,headers=self.headers,data=self.data,files=self.files,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time Out!")
            return  None

    def delete(self):
        try:
            response =requests.delete(self.url,headers=self.headers,data=self.data,files=self.files,timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time Out!")
            return  None





 


























