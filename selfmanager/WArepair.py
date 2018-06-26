# _*_ coding=utf8

import ryanlog
from ryanlog import logger_default

logger_default.info(u'修复模块加载开始')

'''
读取操作系统类型
拷贝现有文件夹至备份文件夹
'''
import configparser
ryanconfig = configparser.ConfigParser()
ryanconfig.read('config/main.conf')
REPAIR = ryanconfig['DEFAULT'].getboolean('REPAIR')
CONNECTOR_TYPE = ryanconfig['DEFAULT'].get('CONNECTOR_TYPE')
SYSTEM_TYPE = ryanconfig['DEFAULT'].get('SYSTEM_TYPE')
logger_default.debug('CONNECTOR_TYPE:'+CONNECTOR_TYPE)
logger_default.debug('REPAIR:'+str(REPAIR))

if (REPAIR==False):
    print(u'修复模式关闭，退出')
    logger_default.info(u'修复模式关闭，退出')
    exit(0)
else:
    #进入修复模式
    print(u'修复模式开启')
    from selfmanager import PID
    print('当前pid=' + str(PID.ryan_pid))
    #判断是否进程存活
    with open(PID.REPAIRPIDFILE,'r') as f:
        OLDPID = f.read()
    
    #print('OLDPID:' + OLDPID)
    logger_default.debug('OLDPID：' + OLDPID)
    #根据操作系统获取的pid检查，判断是否需要修复
    repairmode=0
    if(SYSTEM_TYPE == 'WIN64'):
        print('当前操作系统：WIN64')
        from oscmd.win64.win64 import pidquery
        command = pidquery + ' | findstr ' + OLDPID + ' && echo %ErrorLevel%'
        print('修复命令：' + command)
        from subprocess import getstatusoutput
        cmdstatus, cmdoutput = getstatusoutput(command)
        #cmdoutput = os.system('tasklist | findstr ' + OLDPID )
        #print('1:' + str(cmdstatus))
        #cmdoutput = os.system('echo %ErrorLevel%')
        #print('2:' + str(cmdoutput))
        if(cmdoutput[0:6] != 'python'):
            repairmode = 1
    else:
        print('当前操作系统' + SYSTEM_TYPE)
        from oscmd.linux.linux import pidquery
        command = pidquery + ' | grep ' + OLDPID + ' | grep -v "grep" | wc -l' 
        print('修复命令：' + command)
        from subprocess import getstatusoutput
        cmdstatus, cmdoutput = getstatusoutput(command)
        print('cmdoutput:' + cmdoutput)
        if( 0 == int(cmdoutput)):
            repairmode=1
        
        
#如果进程存活，则退出修复模式
if(repairmode == 0):
    logger_default.info(u'进程存活，无需修复，主进程退出')
    exit(0)
else:
    logger_default.info(u'修复模块加载完成，现在生效的是备份版本')
    '''在操作系统中设置自动任务，定时判断pid进程是否存在
                    如果不存在，则操作系统会自动启动WArepair目录下的备份目录下的main.py，启动的条件由操作系统决定
                    程序是通过main.conf中定义的pid文件的路径来识别 工作版本和备份版本的
    '''
    
