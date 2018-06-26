import configparser
ryanconfig = configparser.ConfigParser()
ryanconfig.read('config/main.conf')
PIDFILE = ryanconfig['DEFAULT'].get('PIDFILE')
SYSTEM_TYPE = ryanconfig['DEFAULT'].get('SYSTEM_TYPE')
if SYSTEM_TYPE == 'WIN64' :
    REPAIRPIDFILE = ryanconfig['WINDIR'].get('REPAIRPID')
else:
    REPAIRPIDFILE = ryanconfig['LINUXDIR'].get('REPAIRPID')

import ryanlog
from ryanlog import logger_default

logger_default.info(u'PID模块加载开始')

import os
ryan_pid = str(os.getpid())
with open(PIDFILE,'w') as f:
    f.write(ryan_pid)

logger_default.info(u'当前主进程PID='+ryan_pid)
logger_default.info(u'PID模块加载完成')