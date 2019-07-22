#coding:utf-8
#__author:"July"
#__date:2019\6\25 0025

import sys
import os
import configparser
import codecs


proDir=os.path.split(os.path.realpath(__file__))[0]
configPath=os.path.join(proDir,'config.ini')


class readConfig:
    def __init__(self):
        with open(configPath)as fd:
            data=fd.read()

        if data[:3]==codecs.BOM_UTF8:
            data=data[3:]
            file=codecs.open(configPath,'w')
            file.write(data)
            file.close()
        fd.close()

        self.cf=configparser.ConfigParser()
        self.cf.read(configPath)


    def get_db(self,name):
        value=self.cf.get("DATABASE",name)
        return value

    def get_email(self,name):
        value=self.cf.get("EMAIL",name)
        return value

    def get_url(self,name):
        value=self.cf.get("HTTP",name)
        return value

# if __name__=="__main__":
#     opera = readConfig()
#     a = opera.get_url('port')
#     print(a)

