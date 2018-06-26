# _*_ coding=utf8

#定义用户类型
class AcceptUser(object):
    '''
        用户权限对象，一共4列
        uid,    remark,     username,    privilege,    mode
        uid(不是所有用户都有),    备注,        用户名(每次更新),     权限清单，以一串01表示是否有权限，    模式
        全都是string类型
    '''
    __slots__=('uid', 'remark', 'username', 'privilege', 'mode')
    
    def __init__(self, remark, uid, username, privilege, mode ):
        '''
            初始化，根据slots的限制，只允许有4列
        '''
        print('acceptuser initialing:' + remark)
        self.uid = uid
        self.remark = remark
        self.username = username
        self.privilege = privilege
        self.mode = mode
    
    def updateUid(self,uid):
        '''
            更新uid
        '''
        self.uid = uid
        
    def updateUsername(self,username):
        '''
            更新username，每次重启服务，都需要更新
        '''
        self.username = username
        
    def updatePrivilege(self, privilege):
        '''
            更新role
        '''
        self.privilege = privilege
        
    def updateMode(self, mode):
        '''
            更新mode
        '''
        self.mode = mode
        
    def __del__(self):
        print('accept_user ' + str(self.remark) +' destroyed')
        pass

