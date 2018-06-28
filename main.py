# _*_ coding: UTF-8 _*_
import os
import sys
import itchat
from header.TurlingState import TLSTATE
from header.TurlingGroup import *
import pickle
from ryanlog import logger_default, logger_textmsg
from commands import checkprivilege
from commands import updateacu
from turling.turling import get_TR_response

from selfmanager import WArepair

from commands.usercmd import grantUser
from commands.command import allprivileges

logger_default.info(u'主进程启动')

#将主进程pid写入文件保存，用于给WArepair判断进程是否存在
print('暂停点1')

#启动子进程，载入计划任务
# todo

#启动操作系统拦截器
# 根据请求的频率等进行拦截，不返回消息，需要记录来消息的人或者ip
# 需要登记操作系统级的连接日志，不过因为微信消息都是从腾讯服务器发来的，所以这个功能暂缓
# todo

#启动消息注册类及拦截器
# 记录每个用户发送消息的频率，通过设定请求数，拒绝超频的请求
# todo

from structure import user
aculist = []        #用户清单

import configparser
ryanconfig = configparser.ConfigParser()
ryanconfig.read('config/main.conf')
SYSTEM_TYPE = ryanconfig['DEFAULT'].get('SYSTEM_TYPE')
SMTPADDR = ryanconfig['DEFAULT'].get('SMTPADDR')
SENDADDR = ryanconfig['DEFAULT'].get('SENDADDR')
SMTPPSWD = ryanconfig['DEFAULT'].get('SMTPPSWD')
if(SYSTEM_TYPE == 'WIN64'):
    USERLIST_FILE = ryanconfig['WINDIR'].get('USERLIST_FILE')
    RYAN_ROOT_DIR = ryanconfig['WINDIR'].get('RYAN_ROOT_DIR')
elif(SYSTEM_TYPE == 'LINUX'):
    USERLIST_FILE = ryanconfig['LINUXDIR'].get('USERLIST_FILE')
    RYAN_ROOT_DIR = ryanconfig['LINUXDIR'].get('RYAN_ROOT_DIR')
else:
    print('ohter os')

#自动热登录
itchat.auto_login(hotReload=True)
#itchat.auto_login(hotReload=False)


print('暂停点2')

#AcceptUserList
#自己的id，比较特殊 uin=1146321620
#百望股份运维部 uin=54915764
#百望运维    uin=3370183581
file_exists = os.path.exists(USERLIST_FILE)
if file_exists == False:
    with open(USERLIST_FILE,'wb') as f:
        defaultline=user.AcceptUser('Roronoa Ryan','1146321620',
                                    'null',allprivileges['ALL'],
                                    TLSTATE['SHUT'],'snowluxury@qq.com')
        #defaultline.printself()
        aculist.append(defaultline)
        pickle.dump(aculist, f)
        f.close()
    print('AcceptUserList.dat not exists')
    logger_default.info(u'用户文件新建成功，1146321620，Roronoa Ryan被添加为默认管理员')
else:
    #print('Loading AcceptUserFile...')
    with open(USERLIST_FILE,'rb') as f:
        aculist=pickle.load(f)
        f.close()
    '''
            清单序号为1的一定是自己
            其他list中的id因为会改变，所以每次需要与里的用户进行更新
            因为除了自己的 Uin=1146321620 不会变之外，其他信息都有可能会变
            #恩，本来有个"微信号"是不会变的也就死paradixrain，但是从返回报文里也抓不到
            所以，要进入，必须得设置对应"备注"，即RemarkName
            需人工保证无重复RemarkName
            启动时候，以RemarkName去找对应UserName（即id)
    '''
    logger_default.info(u'加载用户文件成功，读取用户总数' + str(len(aculist)))
    logger_default.info(u'开始更新aculist')
    #更新username
    friendslist = itchat.get_friends(update=True)
    logger_default.info(u'共获取好友总数：' + str(len(friendslist)))
    for acuindex in range(len(aculist)):
        if(acuindex == 0):
            #print(friendslist[0]['Uin'])
            aculist[0].updateUid(friendslist[0]['Uin'])
            aculist[0].updateUsername(friendslist[0]['UserName'])
            print(friendslist[0]['UserName'])
            logger_default.debug(u'更新自己的username完毕')
        else:
            from itchat import search_friends
            logger_default.debug(u'更新：' + str(aculist[acuindex].remark))
            searchresult=search_friends(remarkName=aculist[acuindex].remark)
            aculist[acuindex].updateUsername(searchresult[0]['UserName'])
            logger_default.debug(u'更新' + str(aculist[acuindex].remark) + '完毕')
    logger_default.info(u'更新aculist结束')
    pass

#测试，打印所有用户
for a in aculist:
    print(a.remark + a.username)
    print(a.privilege)
    print(a.uid)


#import texthandler
#此种引用方式会导致重复reply，所以暂时不剥离每个模块，而是全都放在main底下
'''
注册并处理itchat收到的text类型的消息
'''

@itchat.msg_register(itchat.content.TEXT, isFriendChat=True, isGroupChat=False)
def Ryan_replyText(msg):
    '''
        自动回复主函数，响应群消息和用户消息———只响应未被Mute的用户消息
        1.识别 from user name，
        2.根据配置文件识别 mode
        3.进行响应
        4.捕捉异常
    '''
    #print所有收到的消息
    print(msg)
    
    #global currentdir    #全局当前路径，用来归档文件，切换路径等使用
    #global filereceivedlist    #全局文件清單
    #global sessionlist    #全局session清单
    
    #提取需要的NickName,id和Text
    try:
        toUser = msg['ToUserName']
        NickName = msg['User']['NickName']
        fromuser = msg['FromUserName']
        UserMessage = msg['Text']
        usermode = None
        userprivilege = None
    except:
        logger_textmsg.error("Fail to get msg elements")
        return
    
    print('暂停点3')
    #打印调试
    Receive_msg = NickName + ',id: ' + fromuser + ' said: ' + UserMessage + ' to:' + toUser
    logger_default.debug(Receive_msg)
    reply=aculist[0].username

    #如果是自己发给别人的，则不响应
    if( (fromuser == aculist[0].username) and (toUser != aculist[0].username) ):
        print('not for me')
        return
    
    print('暂停点4')
    #匹配aculist，找到对应的权限和mode
    for findex in range(len(aculist)):
        fuser = aculist[findex]
        print(fuser.remark)
        if(fuser.remark == NickName):
            print('fuser hit')
            fuser.updateUsername(fromuser)
            usermode = fuser.mode
            userprivilege = fuser.privilege
            break
        else:
            pass
    
    
    print('暂停点5')
    #未找到用户
    if(usermode == None):
        print('not listed user')   
        return
    
    #命令拆解
    mycommands = UserMessage.split(' ')
    arglen = len(mycommands)
    
    print('暂停点6')
    #先看是否是chmod
    if(((mycommands[0].upper() == 'CHMOD')) and (arglen<2)):
        reply = 'change mode 参数错误'
        return reply
    if((mycommands[0].upper() == 'CHMOD') and 
       (mycommands[1].upper() in ['TLING', 
                                  'SHUT', 
                                  'OSSYSM', 
                                  'OSSUBP', 
                                  'OSCMMD',
                                  'COMMD',
                                  'COMP', 
                                  'STDY',
                                  'EMAIL'])):
        logger_default.info(u'chmod begins')
        if(checkprivilege.checkPri(userprivilege, UserMessage.upper())):
            print('暂停点8')
            updateacu.updateacu(aculist, findex, None, TLSTATE[mycommands[1].upper()])
            reply = 'changemode to ' + mycommands[1] + ' success'
        else:
            reply = 'change mode 权限不足'
        return reply
    
    print('暂停点18，帮助模式')
    if(UserMessage.upper() == 'LISTMOD'):
        print('暂停点21，帮助模式')
        reply='''使用 chmod + 以下任一模式，进行切换
        'TLING' ,
        'SHUT'  ,
        'OSSYSM',
        'OSSUBP',
        'OSCMMD',
        'COMMD' ,
        'COMP'  ,
        'STDY'  ,
        'EMAIL' ,
        当前模式是：
        ''' + usermode + ',当前权限是：' + str(userprivilege)
        return reply
    
    print('暂停点7')
    if(usermode == TLSTATE['SHUT']):
        reply ='图灵机关闭，可使用chmod开启'
        return reply
    
    print('暂停点13，图灵机模式')
    if(usermode == TLSTATE['TLING']):
        reply = get_TR_response(UserMessage)
        return reply
    
    print('暂停点14，命令模式')
    if(usermode == TLSTATE['COMMD']):
        from commands.usercmd import addUser,delUser,revokeUser
        if( mycommands[0].upper() == 'LISTUSER' ):
            print('暂停点18，命令模式')
            if checkprivilege.checkPri(userprivilege,'LISTUSER'):
                print('暂停点19，命令模式')
                from commands.usercmd import listUser
                if(arglen == 1):
                    print('暂停点22，命令模式')
                    reply = listUser(aculist)
                    print('暂停点24：reply=' + reply)
                elif(arglen >= 2):
                    print('暂停点23，命令模式')
                    reply = listUser(aculist, mycommands[1])
                else:
                    reply = 'listuser unknow error'
            else:
                print('暂停点20，命令模式')
                reply ='LISTUSER 权限不足'
        elif(mycommands[0].upper() == 'ADDUSER' ):
            print('暂停点25，命令模式')
            if (arglen != 2):
                reply = 'ADDUSER 参数不足'
            elif checkprivilege.checkPri(userprivilege,'ADDUSER'):
                addUser(aculist, USERLIST_FILE, mycommands[1], allprivileges['GP_TLING'], TLSTATE['SHUT'],'null')
                #默认值给图灵机权限，且图灵机是关闭状态
            else:
                reply = 'ADDUSER 权限不足'
        elif(mycommands[0].upper() == 'DELUSER' ):
            print('暂停点25，命令模式')
            if (arglen != 2):
                reply = 'DELUSER 参数不对'
            elif checkprivilege.checkPri(userprivilege,'DELUSER'):
                delUser(aculist, USERLIST_FILE, mycommands[1])
                reply = 'DELUSER ' + mycommands[1] + ' FINISHED.'
            else:
                reply = 'DELUSER 权限不足'
        elif(mycommands[0].upper() == 'GRANT' ):
            print('暂停点26，授权模式')
            if( (arglen != 4) and (mycommands[2].upper()!='TO') ):
                reply = 'GRANT 参数不对，应为grant 权限 to somebody'
            elif(checkprivilege.checkPri(userprivilege,'ALL')==False):
                #grant只有超管能做
                reply = 'GRANT 权限不足，只有超管能回收'
            else:
                print('暂停点27，授权模式')
                foundsign = False
                for a in aculist:
                    if(a.remark == mycommands[3]):
                        foundsign = True
                        break
                if (foundsign == False):
                    reply = '用户 ' + mycommands[3] + ' 不存在'
                    return reply
                else:
                    #用户在aculist中
                    reply = grantUser(aculist, USERLIST_FILE, mycommands[3], mycommands[1].upper())
            pass
        elif(mycommands[0].upper() == 'REVOKE'):
            print('暂停点28，收回权限')
            if( (arglen != 4) and (mycommands[2].upper()!='FROM') ):
                reply = 'REVOKE 参数不对，应为revoke 权限  from somebody'
            elif(checkprivilege.checkPri(userprivilege,'ALL')==False):
                #REVOKE只有超管能做
                reply = 'REVOKE 权限不足，只有超管能回收'
            else:
                print('暂停点29')
                foundsign = False
                for a in aculist:
                    if(a.remark == mycommands[3]):
                        foundsign = True
                        break
                if (foundsign == False):
                    reply = '用户 ' + mycommands[3] + ' 不存在'
                else:
                    #用户在aculist中
                    reply = revokeUser(aculist, USERLIST_FILE, mycommands[3], mycommands[1].upper())
        else:
            pass
        return reply
    
    print('暂停点15，操作系统命令模式')
    if(usermode == TLSTATE['OSSYSM']):
        return get_TR_response(UserMessage)
    
    print('暂停点16，公司资料模式')
    if(usermode == TLSTATE['COMP']):
        return get_TR_response(UserMessage)
    
    print('暂停点17，学习资料模式')
    if(usermode == TLSTATE['STDY']):
        return get_TR_response(UserMessage)
    #以下为找到用户的情况，且不是chmod命令的情况
    #命令与权限匹配，看是否允许执行
    # 图灵机模式不判断，RYAN_TL_STATE_TRLN
    return reply

#发送启动消息
logger_default.info(u'WechatAssistant服务启动..')
itchat.send('LuLu started from ' + SYSTEM_TYPE,toUserName=aculist[0].username)

#import filehandler
#开始处理文件类型
@itchat.msg_register(itchat.content.ATTACHMENT, isFriendChat=True, isGroupChat=False)
def Ryan_replyAttachment(msg):
    print(msg)
    try:
        toUser = msg['ToUserName']
        NickName = msg['User']['NickName']
        fromuser = msg['FromUserName']
        attachfile = msg['FileName']
        usermode = None
        userprivilege = None
        emailAddr =None
    except:
        print("Fail to get msg elements")
        logger_default.error(u'抽取附件msg失败..')
        return
    
    Receive_msg = NickName + ',id: ' + fromuser + ' send file: ' + attachfile
    logger_default.info(Receive_msg)
    
    #如果是自己发给别人的，则不响应
    '''为了调试，开启自己发送给自己
    if( (fromuser == aculist[0].username) and (toUser != aculist[0].username) ):
        print('not for me')
        return
    '''
    print('暂停点file : 4')
    #匹配aculist，找到对应的权限和mode
    for findex in range(len(aculist)):
        fuser = aculist[findex]
        print(fuser.remark)
        if(fuser.remark == NickName):
            print('fuser hit')
            fuser.updateUsername(fromuser)
            usermode = fuser.mode
            userprivilege = fuser.privilege
            emailAddr = fuser.EMAIL
            break
        else:
            pass
    
    print('暂停点file : 5')
    #未找到用户
    if(usermode == None):
        print('not listed user')   
        return
    
    #自动处理attahment只有一种场景，自动转发邮箱。
    #因为与手机收到附件不同，python网页版会自动存储对应文档,所以不需要特地归档
    if(usermode == TLSTATE['EMAIL']):
        try:
            print('暂停点 file : 6')
            fileloc= RYAN_ROOT_DIR + msg['FileName']
            msg.download(fileloc)
            print('暂停点 file : 7')
            from commands import sendemail
            subject='从微信转发的邮件'
            attach= RYAN_ROOT_DIR + attachfile
            content='''为了防止被判断为垃圾邮件，也是醉了，要加首歌词
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
            print('SMTPADDR:' + SMTPADDR + ',SENDADDR:' + SENDADDR + ',SMTPPSWD:' + SMTPPSWD + ',emailAddr:' + emailAddr +',subject:'+subject)
            sendemail.send_email(SMTPADDR, SENDADDR, SMTPPSWD, emailAddr, subject, content, attach)
        except Exception as e:
            logger_default.error(e)
    else:
        logger_default.info('不是归档模式，不处理')
    return
    
itchat.run()
logger_default.info(u'主进程结束')
