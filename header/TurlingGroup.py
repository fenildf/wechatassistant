# _*_ coding=utf8

#图灵机应答权限分组
'''
    组别：
    "0000" 自己，所有权限
        "0010" 超管组 ——等同于SELF的权限
    "1000" 普通图灵机管理者——可进行模式切换
    "2000" 普通访问者/群
    "3000-3999" 自定义组别
        "3001" 给刘昶的附件自动转发
    "4000" 普通拒绝者/群
    
    权限次序，从高到底判定：
    自己 > 拒绝 > 自定义 > 普通图灵管理者 > 普通访问者
'''
RYAN_TL_GP_SELF='0000'
RYAN_TL_GP_SUPER=0xFFFF
RYAN_TL_GP_AUTH=0X00
RYAN_TL_GP_NORM='2000'
RYAN_TL_GP_DEFINED_LIUCH='3001'
RYAN_TL_GP_DENY='4000'
