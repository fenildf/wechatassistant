# _*_ coding: UTF-8 _*_

import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from logging import exception
from ryanlog import logger_email

def send_email(smtpHost, sendAddr, password, recipientAddrs, subject='', content='', attach=None):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)
    print('attach:'+ attach)

    # 添加附件，传送D:/软件/yasuo.rar文件
    if attach == None:
        file='C:/Users/Long/Desktop/ml_develop/preview.jpg'
    else:
        try:
            file=attach.split('/')[-1]
            print('attach filename:' + attach + ',file=' + file)
            part = MIMEApplication(open(attach,'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=file)
            msg.attach(part)
        except Exception as e:
            logger_email.error(e)

    try:
        smtp = smtplib.SMTP_SSL()
        smtp.connect(smtpHost, '465')
        smtp.login(sendAddr, password)
        smtp.sendmail(sendAddr, recipientAddrs, str(msg))
        reply='附件' + attach +' 发送至 ' + recipientAddrs + ' 成功！'
        logger_email.info(reply)
    except Exception as e:
        reply='发送失败'
        logger_email.error(e)
    finally:
        smtp.quit()
        logger_email.info('smtp quit')
    return reply
