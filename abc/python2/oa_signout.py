# -*- coding: cp936 -*-
import urllib  
import urllib2  
import cookielib
import re
def sign(data,flag):
    cj = cookielib.CookieJar()
    path='http://192.168.2.253:8099/logincheck.php'
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
    urllib2.install_opener(opener)  
    req = urllib2.Request(path, data)
    ht=urllib2.urlopen(req).read()
    log=urllib2.urlopen('http://192.168.2.253:8099/general/ipanel/pheader.php?ISPIRIT=').read()
    xia=urllib2.urlopen('http://192.168.2.253:8099/general/attendance/personal/duty/submit.php?REGISTER_TYPE=2').read()
    # signin=urllib2.urlopen('http://192.168.2.253:8099/general/attendance/personal/duty/submit.php?REGISTER_TYPE=1').read()
    print "ǩ��"
    rel=urllib2.urlopen('http://192.168.2.253:8099/general/relogin.php').read()
    lo=urllib2.urlopen('http://192.168.2.253:8099/general/attendance/personal/duty/').read()
    try:
        s=re.findall('<span.*on_status_span.*?title="(.*)',log)[0]
        print '\t',s
    except:
        print '��½ʧ�ܡ�'
if __name__=='__main__':
    fi=open('./passwd','r')
    if not fi:
        pass
    else:
        for line in fi:
            line=line.replace('\n','')
            info=line.split(',')
            post_data = urllib.urlencode({
                'UNAME': info[0],
                'PASSWORD': info[1],
                'UI': '0',
                'submit':'��½'})
            sign(post_data,1)
    fi.close()
