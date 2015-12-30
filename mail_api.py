#coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from Config import *

def send_mail(receiv_list, subject, content):
  msg = MIMEText(content,'html','utf-8')
  msg['Subject'] = subject
  msg['From'] = From_Address
  msg['To'] = ';'.join(receiv_list)
  try:
    server = smtplib.SMTP(Smtp_Server)
    server.login(Account_Name, Account_Pwd)
    server.sendmail(From_Address, receiv_list, msg.as_string())
    server.close()
    return True
  except Exception as e:
    print e
    return False


if __name__=='__main__':
  content = '<html><h1>你好</h1></html>'
  send_mail(To_Address_List, '主题', content)
