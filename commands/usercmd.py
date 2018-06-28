# _*_ coding=utf8
from ryanlog import logger_usercmd
from structure import user
import pickle
from commands.command import allprivileges

def listUser(aculist, remark=None):
    reply=''
    if(remark == None):
        print('listuser stop1')
        reply = '总用户数:' + str(len(aculist)) +'\n'
        for acu in aculist:
            print('acu.remark:' +acu.remark)
            print('acu.mode:' + acu.mode)
            reply += acu.remark + ':' + str(acu.mode) + ',' +str(acu.privilege)+',' +str(acu.EMAIL)+ '\n'
    else:
        print('listuser stop2')
        for acu in aculist:
            if(acu.remark == remark):
                reply = acu.remark + ':' + acu.mode + ',' +str(acu.privilege)
                break
        if( reply == ''):
            reply= '用户' + remark + '未找到'
    logger_usercmd.debug(reply)
    return reply

def addUser(aculist, USERLIST_FILE, remark, privilege=None, mode=None, email=None):
    try:
        from itchat import search_friends
        searchresult=search_friends(remarkName=remark)
        print('adduser stop1')
        for a in aculist:
            print(a.remark)
        newuser=user.AcceptUser(remark, '', searchresult[0]['UserName'], privilege, mode, email)
        aculist.append(newuser)
        print('adduser stop2')
        for a in aculist:
            print(a.remark)
        with open(USERLIST_FILE,'wb') as f:
            print('adduser stop3')
            pickle.dump(aculist, f)
            f.close()
    except Exception as e:
        print('adduser stop3')
        logger_usercmd.debug(e)
    logger_usercmd.info('ADDUSER' + remark + 'with privilege:' + str(privilege) + ', mode:' + str(mode))
    return


def delUser(aculist, USERLIST_FILE, remark):
    try:
        print('deluser stop1')
        for index in range(len(aculist)):
            if( aculist[index].remark == remark):
                print('deluser stop2')
                logger_usercmd.info('DELUSER' + remark + 'FOUND')
        del(aculist[index])
        print('adduser stop2')
        with open(USERLIST_FILE,'wb') as f:
            print('adduser stop3')
            pickle.dump(aculist, f)
            f.close()
    except Exception as e:
        print('deluser stop3')
        logger_usercmd.debug(e)
    logger_usercmd.info('DELUSER ' + remark +' FINISHED')
    return

def grantUser(aculist, USERLIST_FILE, remark, privilege=None):
    try:
        print('grantuser stop2')
        for index in range(len(aculist)):
            if( aculist[index].remark == remark):
                print('grantuser stop2')
                logger_usercmd.info('GRANTUSER' + remark + 'FOUND')
                if(privilege[0:2] != '0x'):
                    print('grantuser stop3')
                    #以字符串形式表示的权限，去command表里找
                    #类似'CHMOD TLING'的权限，因为存在空格，所以不能使用此种方式
                    try:
                        pri = allprivileges[privilege]
                        aculist[index].privilege=(aculist[index].privilege | pri)
                    except KeyError as e:
                        logger_usercmd.error('grant error.')
                        logger_usercmd.error(e)
                        reply = '权限不在清单中，请使用 类似0x0000方式赋权'
                        return reply
                else:
                    #以数值表示的权限
                    try:
                        print('aculist[index].privilege:')
                        print(type(aculist[index].privilege))
                        print(aculist[index].privilege)
                        print('privilege:')
                        print(type(privilege))
                        print(privilege)
                        aculist[index].privilege=(aculist[index].privilege | int(privilege,16))
                    except Exception as e:
                        logger_usercmd.error(e)
                        return 'grant error'
                break
        with open(USERLIST_FILE,'wb') as f:
            print('grantuser stop4')
            pickle.dump(aculist, f)
            f.close()
    except Exception as e:
        print('grantuser stop5')
        logger_usercmd.error(e)
    reply = 'GRANTUSER' + remark + 'with privilege:' + str(privilege)
    logger_usercmd.info(reply)
    return reply


def revokeUser(aculist, USERLIST_FILE, remark, privilege=None):
    try:
        print('revokeUser stop1')
        for index in range(len(aculist)):
            if( aculist[index].remark == remark):
                print('revokeUser stop2')
                logger_usercmd.info('REVOKEUSER' + remark + 'FOUND')
                if(privilege[0:2] != '0x'):
                    print('revokeuser stop3')
                    #以字符串形式表示的权限，去command表里找
                    #类似'CHMOD TLING'的权限，因为存在空格，所以不能使用此种方式
                    try:
                        pri = allprivileges[privilege]
                        aculist[index].privilege=((aculist[index].privilege | pri) - pri)
                    except KeyError as e:
                        logger_usercmd.error('revoke error.')
                        logger_usercmd.error(e)
                        reply = '权限不在清单中，请使用 类似0x0000方式赋权'
                        return reply
                else:
                    #以数值表示的权限
                    try:
                        aculist[index].privilege=((aculist[index].privilege | int(privilege)) -int(privilege))
                    except Exception as e:
                        logger_usercmd.error(e)
                        return 'revoke error'
                break
        with open(USERLIST_FILE,'wb') as f:
            print('revokeUser stop4')
            pickle.dump(aculist, f)
            f.close()
    except Exception as e:
        print('revokeUser stop5')
        logger_usercmd.error(e)
    reply = 'revokeUser' + remark + 'with privilege:' + str(privilege)
    logger_usercmd.info(reply)
    return reply



def updateemail(aculist, USERLIST_FILE, remark, NEWEMAIL):
    try:
        print('updateemail stop1')
        for index in range(len(aculist)):
            if( aculist[index].remark == remark):
                print('updateemail stop2')
                logger_usercmd.info('updateemail' + remark + 'FOUND')
                aculist[index].EMAIL = NEWEMAIL
                break
        with open(USERLIST_FILE,'wb') as f:
            print('updateemail stop3')
            pickle.dump(aculist, f)
            f.close()
    except Exception as e:
        print('updateemail stop4')
        logger_usercmd.ERROR(e)
    logger_usercmd.info('updateemail ' + remark +' FINISHED')
    return
