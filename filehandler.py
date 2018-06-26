
@itchat.msg_register(itchat.content.ATTACHMENT, isFriendChat=True, isGroupChat=False)
def Ryan_getFile(msg):
    '''
        所有文件都临时下载到 RYAN_ROOT_DIR，系统中会建一个默认的bash，对于没有归档的文件进行删除
    '''
    #提取需要的NickName,id和Text
    NickName=''
    fromuser=''
    UserMessage = ''
    toUser=''
    print('File msg:')
    print(msg)
    try:
        toUser = msg['ToUserName']
        NickName = msg['User']['NickName']
        fromuser = msg['FromUserName']
        UserMessage = msg['FileName']
    except:
        print("Fail to get msg elements")
        return
    
    #打印调试
    Receive_msg = NickName + ',id: ' + fromuser + ' send file: ' + UserMessage
    
    role = getRolebyuid(aculist, fromuser)     #默认角色——读aculist
    
    #debug
    print('Receive_msg' + Receive_msg + ' role '  + role)

    #Step1. 无权限者，不响应
    if((role == None)):
        print('step1')
        #reply = reply + '.step1'
        return
    

    #Step2. 归档至默认目录，往filereceivedlist中添加一笔
    fileloc= RYAN_ROOT_DIR + msg['FileName']
    print(fileloc)
    msg['Text'](fileloc)
    #return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
    #itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])
    fileinfo=[fromuser,toUser,fileloc]
    filereceivedlist.append(fileinfo)
    reply='archieve success'
    
    #debug，打印文件
    print('allfile:\n')
    for f in filereceivedlist:
        reply = reply + f[2] + '\n'
    return reply
