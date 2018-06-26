# _*_ coding=utf8
'''
注册并处理itchat收到的text类型的消息
'''

import itchat
from ryanlog import logger_textmsg
#from main import aculist
#print(aculist[0].username)

@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=False)
def Ryan_replyPerson(msg):
    '''
        自动回复主函数，响应群消息和用户消息———只响应未被Mute的用户消息
        1.识别 from user name，
        2.根据配置文件识别 mode
        3.进行响应
        4.捕捉异常
    '''
    #print所有收到的消息
    print(msg)
    
    global currentdir    #全局当前路径，用来归档文件，切换路径等使用
    global filereceivedlist    #全局文件清單
    #global aculist    #全局用户清单
    from main import aculist
    print(aculist[0].username)
    global sessionlist    #全局session清单
    
    #提取需要的NickName,id和Text
    NickName=''
    fromuser=''
    UserMessage = ''
    toUser=''
    try:
        toUser = msg['ToUserName']
        NickName = msg['User']['NickName']
        fromuser = msg['FromUserName']
        UserMessage = msg['Text']
    except:
        logger_textmsg.debug("Fail to get msg elements")
        return
    
    #打印调试
    Receive_msg = NickName + ',id: ' + fromuser + ' said: ' + UserMessage + ' to:' + toUser
    logger_textmsg.debug(Receive_msg)
    #reply= Receive_msg
    reply=aculist[0].username
    print('reply is' + reply)
    #role = getRolebyuid(aculist, fromuser)     #默认角色——读aculist
    return reply