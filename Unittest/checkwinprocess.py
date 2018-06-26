#-*- coding:utf-8 -*-  
  
import win32com.client  
  
def check_exsit(process_name):
    '''判断windows进程是否存在
    '''  
    WMI = win32com.client.GetObject('winmgmts:')  
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)  
    if len(processCodeCov) > 0:  
        print '%s is exists' % process_name  
    else:  
        print '%s is not exists' % process_name  
  
if __name__ == '__main__':  
    check_exsit('coral.exe')  