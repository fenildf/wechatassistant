main.conf字段含义说明
[DEFAULT]
RYAN_CONNECTOR_TYPE=FILE
# FILE / MYSQL / ORACLE 等方式来读取用户清单，权限等

SYSTEM_TYPE=WIN64
# WIN64 / UBUNTU / REDHAT 等方式来确定直接调用命令的执行方式主要体现在 OS.CMD, SUPPROCESS等

REPAIR = True
# 开启自动修复

[WINDIR]
RYAN_ROOT_DIR=d:/FILEDIR/wechatdir/
RYAN_FILE_DIR=d:/FILEDIR/RyanFiles/
RYAN_ALLFILE_TREE=${RYAN_FILE_DIR}/ALLFILETREE.TXT
RYAN_ALLFILE_LS=${RYAN_FILE_DIR}/ALLFILELS.TXT
USERLIST_FILE=${RYAN_ROOT_DIR}/UserList.dat
USERSES_FILE=${RYAN_ROOT_DIR}/UserSes.dat
REPAIRDIR = D:/work/workspace/WArepair

[LINUXDIR]
RYAN_ROOT_DIR=/home/ryan/wechatdir/
RYAN_FILE_DIR=/home/ryan/RyanFiles/
RYAN_ALLFILE_TREE=${RYAN_FILE_DIR}/ALLFILETREE.TXT
RYAN_ALLFILE_LS=${RYAN_FILE_DIR}/ALLFILELS.TXT
USERLIST_FILE=${RYAN_ROOT_DIR}/UserList.dat
USERSES_FILE=${RYAN_ROOT_DIR}/UserSes.dat
REPAIRDIR = 

[MYSQL]
host = 127.0.0.1
port = 3306
user = root
passwd = Admin123
db = testdb
charset = utf8

[REPAIR]
REPAIRDIR = D:/work/workspace/WArepair
