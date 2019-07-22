# #coding:utf-8
# #__author:"July"
# #__date:2019\7\3 0003
#
# import os,sys
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from datetime import datetime
# import threading
# import readConfig
# from common.Log import MyLog
# import zipfile #压缩文件
# import glob #文件搜索
#
# localReadConfig = readConfig.readConfig()
#
# class Email:
#     def __init__(self):
#         global host,user,password,port,sender,title,content
#         host = localReadConfig.get_email('mail_host')
#         user = localReadConfig.get_email('mail_user')
#         password = localReadConfig.get_email("mail_password")
#         port = localReadConfig.get_email('mail_port')
#         title = localReadConfig.get_email('subject')
#         content = localReadConfig.get_email('content')
#         self.value =  localReadConfig.get_email("receiver")
#         self.receiver = []
#         #获取收件人列表
#         for n in str(self.value).split('/'):
#             self.receiver.append(n)
#
#         date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.subjcet = title + ' ' + date
#         self.log = MyLog.get_log()
#         self.logger = self.logger.get_logger()
#         self.msg = MIMEMultipart('mixed')
#
#     def config_header(self):
#         self.msg['subject'] =  self.subjcet
#         self.msg['from'] = user
#         self.msg['to'] = ";".join(self.receiver)
#
#     def config_content(self):
#         content_plain = MIMEText(content,'plain','utf-8')
#         self.msg.attach(content_plain)
#
#     # def check_file(self):
#     #     reportpath =  self.log.get_report_path()
#     #     if os.path.isfile(reportpath) and not os.stat(reportpath) ==0:
#     #         return True
#     #     else:
#     #         return False
#
#     def send_email(self):
#         self.config_header()
#         self.config_content()
#         try:
#             smtp = smtplib.SMTP()
#             smtp.connect(host)
#             smtp.login(user,password)
#             smtp.sendmail(sender,self.receiver,self.msg.as_string())
#             smtp.quit()
#             self.logger.info("the test report has send to developer by email")
#         except Exception as ex:
#             self.logger.error(str(ex))
#
#
#     class MyEmail:
#         global email
#         email =  None
#
#         mutex =  threading.Lock()
#
#         @staticmethod
#         def get_email():
#             if MyEmail.email == None:
#                 MyEmail.mutex.acquire()
#                 MyEmail.email = Email()
#                 MyEmail.mutex.release()
#
#     if __name__=="__main__":
#         email = MyEmail.get_email()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
