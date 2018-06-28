# _*_ coding=utf8
'''
记录所有可被解析的命令，及对应的权限位置，权限位置为AcceptUser对象中的privilege
当对应的位置为1时，则解析对应命令
默认最大权限是给自己的0xFFFFFFFFFFFF
可存储48个权限位，应该够用了
'''

#权限，含单个权限及组合权限
allprivileges={
'ALL':                   0xFFFFFFFFFFFF,                #所有权限
'CHMOD TLING':           0x0001,                #图灵模式
'CHMOD SHUT':            0x0002,                #关机模式
'CHMOD OSSYSM':          0x0004,                #OSsystem模块模式
'CHMOD OSSUBP':          0x0008,                #OSsubprocess模块模式
'CHMOD OSCMMD':          0x0010,                #OScommand模块模式
'CHMOD COMP':            0x0020,                #公司资料模式
'CHMOD STDY':            0x0040,                #学习资料模式
'LISTMOD':              0x0080,                #帮助模式
'ADDUSER':              0x0200,                #创建用户
'DELUSER':              0x0400,                #删除用户
'LISTUSER':             0x0800,                #列示用户
'CHMOD COMMD':          0x1000,                #命令模式
'GRANT':                0X2000,                #授权用户    
'REVOKE':               0x4000,                #收回用户权限
'CHMOD EMAIL':          0x8000,                 #自动回复邮件模式    
'GP_TLING':             0x000000000111,               #切换图灵及关闭图灵机权限
'GP_COMMD':             0x000000000F80,               #使用LISTMOD至LISTUSER的权限
}
