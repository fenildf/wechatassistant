# _*_ coding=utf8
from commands import command
from commands.command import allprivileges

def checkPri(userprivilege, usercommand):
    pri=command.allprivileges[usercommand]
    if((userprivilege & pri)==pri):
        print('match')
        return True
    return False

if(checkPri(0x00000001, 'CHMOD TLING')):
    print('match2')
else:
    print('not match')
    
try:
    print(allprivileges['ALL']+'1')
except KeyError as e:
    print('keynot found')
except Exception as e1:
    print(e1)

a='good 0x0001'
print(a)
b=a.split(' ')
for b1 in b:
    print(type(b1))
    print(b1[0:2])
    
    
c=0x0001
d=0x0011
e=0x0101
print(c | d)
print((c | d)-d)

print((e | c)-c)
print((e | d)-d)