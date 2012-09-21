# -*- coding: cp936 -*-
import urllib  
import urllib2  
import cookielib
import re
def sign(data,flag):
    cj = cookielib.CookieJar()
    path='http://192.168.2.253:8099/logincheck.php'
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11')]
    urllib2.install_opener(opener)  
    req = urllib2.Request(path, data)
    ht=urllib2.urlopen(req).read()
    log=urllib2.urlopen('http://192.168.2.253:8099/general/ipanel/pheader.php?ISPIRIT=').read()
    if not flag:
        #print '签退'.decode('gbk').encode('utf8'),':'
        print "签退"
        xia=urllib2.urlopen('http://192.168.2.253:8099/general/attendance/personal/duty/submit.php?REGISTER_TYPE=2').read()
    elif flag==1:
        signin=urllib2.urlopen('http://192.168.2.253:8099/general/attendance/personal/duty/submit.php?REGISTER_TYPE=1').read()
        #print '签到'.decode('gbk').encode('utf8'),':'
        print "签到"
    rel=urllib2.urlopen('http://192.168.2.253:8099/general/relogin.php').read()
    lo=urllib2.urlopen('http://192.168.2.253:8099/general/attendance/personal/duty/').read()
    try:
        s=re.findall('<span.*on_status_span.*?title="(.*)',log)[0]
    # s=s.decode('gb2312').encode('utf8')
        print '\t',s
    except:
        print '登陆失败。'
# 包含用户名密码的post数据
# post_data_wsz = urllib.urlencode({
#     'UNAME': 'wsze',
#     'PASSWORD': '000000aaa',
#     'UI': '0',
#     'submit':'登陆'})
# 0 签退 1签到
if __name__=='__main__':
    f=input('''
输入0或者1,
0签退，
1签到
''')
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
                'submit':'登陆'})
            sign(post_data,f)
            try:
                input('回车继续。')
            except:
                pass
    fi.close()
