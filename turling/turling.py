# _*_ coding=utf8
import requests
from ryanlog import logger_turling

def get_TR_response(msg):
    '''
        用于获取图灵机器人消息
    '''
    apiUrl='http://www.tuling123.com/openapi/api'
    data={
        'key'    : 'ffeac15468b9471ca3b0b1be71a657e8', #我在tuling123上注册的机器人的id
        'info'    : msg,
        'userid': 'wechat-rebot-lulu', #露露
        }
    try:
        r=requests.post(apiUrl,data=data).json()
        reply = r.get('text')
        logger_turling.info(reply)
        return reply
    except Exception as e:
        logger_turling.info(e)
        return '机器人无响应'
