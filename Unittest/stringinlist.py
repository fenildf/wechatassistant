# _*_ coding=utf8

mycommand = 'commd'
commands = ['TLING', 'SHUT', 'OSSYSM', 'OSSUBP', 'OSCMMD','COMMD','COMP', 
            'STDY']
if (mycommand.upper() in commands):
    print(u'chmod begins')
else:
    print( 'not in')
    
    

attach='/home/ryan/filedir/priview.jpg'
file=attach.split('/')[-1]
print(file)