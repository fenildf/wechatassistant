# _*_ coding=utf8
import os
import pickle
from ryanlog import logger_updateacu

def updateacu(aculist, index, newpriv, newmode):
    logger_updateacu.info(u'开始更新用户 ' + aculist[index].remark )
    
    USERLIST_FILE=''
    import configparser
    ryanconfig = configparser.ConfigParser()
    ryanconfig.read('config/main.conf')
    SYSTEM_TYPE = ryanconfig['DEFAULT'].get('SYSTEM_TYPE')
    if(SYSTEM_TYPE == 'WIN64'):
        USERLIST_FILE = ryanconfig['WINDIR'].get('USERLIST_FILE')
    elif(SYSTEM_TYPE == 'LINUX'):
        USERLIST_FILE = ryanconfig['LINUXDIR'].get('USERLIST_FILE')
    else:
        print('unknow system_type')
        pass
    
    print('暂停点9')
    
    try:
        with open(USERLIST_FILE,'wb') as f:
            print('暂停点11')
            if(newpriv != None):
                print('更新  newpriv')
                aculist[index].privilege = newpriv
            if(newmode != None):
                print('更新  newmode')
                aculist[index].mode = newmode
                pickle.dump(aculist, f)
            f.close()
    except Exception as e:
        print(e)
        return False

    print('暂停点10')
    logger_updateacu.info(u'文件更新成功，用户 ' + aculist[index].remark + ' 变更完毕')
    return True