#coding:utf-8
#__author:"July"
#__date:2019\7\2 0002


import sys,os
# AbsolutePath = os.path.abspath(__file__)
# SuperiorCatalogue = os.path.dirname(AbsolutePath)
# BaseDir = os.path.dirname(SuperiorCatalogue)
# sys.path.insert(0,BaseDir)
import xlrd
import xlwt

from xlrd import open_workbook

import common
from common.configHttp import ConfigHttp
import readConfig as readConfig
from common.Log import MyLog



localReadConfig = readConfig.readConfig()
proDir = readConfig.proDir
localConfigHttp = common.configHttp.ConfigHttp
log = MyLog.get_log()
# logger = common.Log.logger.get_logger()

class OperationExcel:
    def __init__(self,xls_name,sheet_id):
            file_name = os.path.join(proDir,'Cases',xls_name)
            # print(file_name)
            self.file = xlrd.open_workbook(file_name,'utf-8')
            self.sheet = self.file.sheet_by_index(sheet_id)
            # print(self.sheet)

    #获取单元格行数
    def get_lines(self):
        rows = self.sheet.nrows
        return rows

    #获取单元格内容
    def get_cell_value(self,row,col):
        cell_data = self.sheet.cell_value(row,col)
        return cell_data

    #获取某列数据
    def get_col(self,col):
        cls =[]
        nrows = self.sheet.nrows
        for i in range(nrows):
            if self.sheet.row_values(i)[0] !=u"Case_Name":
                cls.append(self.sheet.row_values(i))
        return cls

#
# class WriteExcel:
#     def __init__(self,xls_name,sheet_name):
#         file_name = os.path.join(proDir,'Cases',xls_name)
#         self.file = xlrd.open_workbook(file_name,'utf=8')
#         self.sheet = self.file.sheet_by_name(sheet_name)




# if __name__ == '__main__':
#     h = OperationExcel("Login.xlsx",0)
#     a = h.get_lines()
#     print(a)

















# if __name__=="__main__":
#     opera = OperationExcel
#     print(opera.get_tables('Login.xlsx'))
















