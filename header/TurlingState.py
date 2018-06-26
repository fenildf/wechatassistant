# _*_ coding=utf8

#预定义当前会话图灵机状态
'''
    针对每个会话，都有一个状态
    命令解析状态：
    "0000"    shut    关闭状态——假关闭（真关闭需要在手机上logout)
    "1000  os    超级模式——直接系统命令模式——os.Popen
        10001 os.system os.system
        10002 os.subprocess subprocess.Popen
        10003 os.getstatusoutput subprocess.getstatusoutput
    "2000  command    Ryan自定义的命令模式，命令如下：
        adduser username
        listuser
        deluser username
        showmod
        chgpauth user 将用户设置为auth组
        chgpnorm user 将用户设置为normal组
    "3000  turling    外挂图灵机器人模式
    "4000  company    Ryan自定义的业务应答模式——可再下挂不同的分类
    "5000"    study    学习资料检索模式
'''
TLSTATE={
'SHUT':'RYAN_TL_STATE_SHUT',
'OS':'RYAN_TL_STATE_OS',
'OSSYSM':'RYAN_TL_STATE_OS_SYSTEM',
'OSSUBP':'RYAN_TL_STATE_OS_SUBPROCESS',
'OSCMMD':'RYAN_TL_STATE_OS_COMMANDS',
'COMMD':'RYAN_TL_STATE_COMD',
'TLING':'RYAN_TL_STATE_TRLN',
'COMP':'RYAN_TL_STATE_COMP',
'STDY':'RYAN_TL_STATE_STDY',
}