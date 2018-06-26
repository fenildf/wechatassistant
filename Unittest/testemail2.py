#!/usr/bin/python3 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
#mail_host="smtp.163.com"  #设置服务器
mail_host="smtp.qq.com"  #设置服务器
mail_user="1651168647"    #用户名
mail_pass="msjvhktotstgegji"   #口令，snowluxury@qq.com的授权码

sender = 'snowluxury@qq.com'
receivers = ['paradixrain@qq.com','larmack@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('发给自己的备忘录', 'plain', 'utf-8')
message['From'] = Header("北河三", 'utf-8')
message['To'] =  Header("自己的qq邮箱", 'utf-8')

subject = '发给自己的备忘录'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL() 
    smtpObj.connect(mail_host, 465)    # 25 为 163的SMTP 端口号，465是qq的
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
    smtpObj.quit()
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
    print(e)
finally:
    pass
