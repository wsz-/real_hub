# -*- coding: cp936 -*-
import urllib
import urllib2
import re
import cookielib
import threading
def look():
    import sqlite3
    import time
    now=time.strftime('%x-%X',time.localtime())
    con=sqlite3.connect('d:/home/data.db3')
    cur=con.cursor()
    d=cur.execute('select * from baidu_linukso')
    for i in d.fetchall():
        print i
    con.close()
def save(lst):
    import sqlite3
    import time
    now=time.strftime('%x-%X',time.localtime())
    con=sqlite3.connect('d:/home/data.db3')
    con.text_factory = str
    cur=con.cursor()
    sql='''insert into baidu_linukso (id,date,count) values(?,?,?)'''
    try:
        cur.execute('create table if not exists baidu_linukso (id,date,count)')
    except:
        pass
    for k,v in lst.items():
        cur.execute(sql,(k,now,v))
    con.commit()
    con.close()
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
# s= urllib2.urlopen('http://www.baidu.com').read()
header={'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2'}
def f(i):
    try:
        so=urllib2.urlopen('http://tieba.baidu.com/f?kw=linukso&pn=%s',str(i)).read()
        title=re.compile(r'tb_icon_author.*?><a.*?>(.*?)</a>')
        l=title.findall(so)
        all.extend(l)
    except:
        return None
# f(0)
all=[]
thread_pool=[]
def getF(i):
    def real():
        f(i)
    return real
for i in range(0,54):
    ff=getF(i*50)
    t=threading.Thread(target=ff)
    thread_pool.append(t)
l_s={}
def to_dict():
    for t in thread_pool:
        t.start()
        t.join()
    for i in all:
        i=i.decode('gbk').encode('utf8')
        try:
            l_s[i]=l_s[i]+1
        except:
            l_s[i]=1
    save(l_s)
    for k,v in l_s.items():
        print k,v
main_t=threading.Thread(target=to_dict)
main_t.start()
