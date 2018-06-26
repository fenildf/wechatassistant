#!/usr/bin/python
# -*- coding: UTF-8 -*-
#试验成功
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(smtpHost, sendAddr, password, recipientAddrs, subject='', content=''):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)

    # 添加附件，传送D:/软件/yasuo.rar文件
    part = MIMEApplication(open('C:/Users/Long/Desktop/ml_develop/preview.jpg','rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="preview.jpg")
    msg.attach(part)

    smtp = smtplib.SMTP_SSL()
    smtp.connect(smtpHost, '465')
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    print("发送成功！")
    smtp.quit()

try:
    subject = '我用smtp给自己发送的第4封邮件'
    content = '''这是一封来自 我自己编写的测试邮件，try 4。
如果那两个字没有颤抖
我不会发现我难受
怎么说出口
也不过是分手
如果对于明天没有要求
牵牵手就像旅游
成千上万个门口
总有一个人要先走
怀抱既然不能逗留
何不在离开的时候
一边享受 一边泪流
十年之前
我不认识你 你不属于我
我们还是一样
陪在一个陌生人左右
走过渐渐熟悉的街头
十年之后
我们是朋友 还可以问候
只是那种温柔
再也找不到拥抱的理由
情人最后难免沦为朋友
怀抱既然不能逗留
何不在离开的时候
一边享受 一边泪流
十年之前
我不认识你 你不属于我
我们还是一样
陪在一个陌生人左右
走过渐渐熟悉的街头
十年之后
我们是朋友 还可以问候
只是那种温柔
再也找不到拥抱的理由
情人最后难免沦为朋友
直到和你做了多年朋友
才明白我的眼泪
不是为你而流
也为别人而流 
    '''
    send_email('smtp.qq.com','1651168647@qq.com', 'msjvhktotstgegji', 'paradixrain@qq.com;larmack@163.com', subject, content)
except Exception as err:
    print(err)