# _*_ coding=utf8

#import configparser
import logging
from logging import config


#读取config中的日志文件名和级别
#ryanconfig = configparser.ConfigParser()
#ryanconfig.read('../config/main.conf')
#RYAN_CONNECTOR_TYPE = ryanconfig['DEFAULT'].get('RYAN_CONNECTOR_TYPE')

#debug
#print(ryanconfig.sections())
#print(RYAN_CONNECTOR_TYPE)

# 读取日志配置文件内容
logging.config.fileConfig('config/mainlog.conf')

# 从配置文件中读取创建一个日志器logger
logger_fixer = logging.getLogger('fixer')
logger_default = logging.getLogger('root')
logger_textmsg = logging.getLogger('textmsg')
logger_filemsg = logging.getLogger('filemsg')
logger_updateacu = logging.getLogger('updateacu')
logger_turling = logging.getLogger('turling')
logger_usercmd = logging.getLogger('usercmd')

# DEBUG 日志输出
logger_default.info(u'日志模块加载开始')

#定义输出日志的handler和输出console的handler


#定义各类filter来决定是否打印对应模块的日志

logger_default.info(u'日志模块加载完成')


