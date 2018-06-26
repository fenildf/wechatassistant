# _*_ coding=utf8
from header import TurlingState
from commands import command

'''
def checkPri(userprivilege, usercommand):
    for cmd in command.allprivileges:
        if (cmd[0] == usercommand.upper()):
            print('cmd:' +str(cmd))
            print('usercommand:'+usercommand)
            print(userprivilege)
            if((userprivilege & cmd[1])==cmd[1]):
                print('match')
                return True
    return False
'''

def checkPri(userprivilege, usercommand):
    pri=command.allprivileges[usercommand]
    if((userprivilege & pri)==pri):
        print('match')
        return True
    return False