# -*- coding: cp936 -*-
import threading
import re
from subprocess import check_output
o=check_output('ping 192.168.2.240')
r=re.compile('TTL')
di=[]
c=0
class pingC(threading.Thread):
    def __init__(self,ip):
        threading.Thread.__init__(self)
        self.ip=ip
    def run(self):
        try:
            o=check_output(' '.join(['ping','-n','1',self.ip]))
            # print threading.activeCount()
            if re.findall('TTL',o):
                # print self.ip,'\n'
                di.append(self.ip)
        except:
            pass
def test_ping():
    for i in range(1,255):
        t=pingC('192.168.2.'+str(i))
        t.start()
        while threading.activeCount() >= 2:
            pass
        print '有',len(di),'个主机在线。'
        print '\n'.join(di)
def func():
    import time
    for i in range(1,10):
        if i==5:
            time.sleep(1)
        print 'aaa\n'
def func_1():
    for i in range(1,10):
        print 'bbb\n'
def test_thread():
    t=threading.Thread(target=func)
    t1=threading.Thread(target=func_1)
    t.start()
    t1.start()
local=threading.local()
local.tname='main'
def t_local():
    def func():
        local.tname='t_local'
        print local.tname
    t=threading.Thread(target=func)
    t.start()
    t.join()
    print local.tname,1
if __name__=='__main__':
    # test_thread()
    # t_local()
