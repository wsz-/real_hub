# -*- coding: cp936 -*-
import mysql
import mysql.connector
import datetime
from string import Template
from sys import argv
def start(cur,tablelist):
    time=datetime.datetime
    start=time.now()
    changer={'var':'String',
             'dec':'BigDecimal',
             'cha':'String',
             'tex':'String',
             'blo':'byte[]',
             'int':'Integer',
             'int':'Integer',
             'tin':'Integer',
             'sma':'Integer',
             'med':'Integer',
             'bit':'Integer',
             'boo':'Integer',
             'dou':'Double',
             'flo':'Float',
             'big':'Interger',
             'var':'String',
             'dat':'String'}
    for table in tablelist:
        try:
            sql='show fields from '+str(table)
            cur.execute(sql)
            result=cur.fetchall()
            print('表：'+table)
            with open('./python/'+table+'.java',mode='w+') as out:  
                for tup in result:
                    #print(tup)
                    st=''
                    up=False;
                    for i in tup[0].lower():
                        if up==True:
                            st=st+i.upper()
                            up=False
                        elif i!='_':
                            st=st+i
                        else:
                            up=True
                    tt='private '+changer[tup[1][0:3]]+' ' +st+';'
                    print(tt)
                    out.write(tt)
        except Exception as err:
            with open('xxx.txt',mode='a') as out_err:
                print(str(err))
                out_err.write(str(err))
    end=time.now()
    print(end-start)
def main1():
    try :
        info=[]
        if len(argv)==1:
            ttt=raw_input('''
    仅适用于mysql。
    选择模式：
    1.连接xedk，指定表
    11.导出xedk中所有表的字段
    2.连接cms，指定表
    22.导出cms中所有表的字段
    3.手动输入用户名，密码，数据库。指定表
    33.连接数据库，并导出所有表的字段
    ''');
        else:
            print('不需要参数。');
            exit()
        ttt=int(ttt)
        if ttt==1 or ttt==11:
            info=['xedk','admin','xedk']
        elif ttt==2 or ttt==22:
            info=['cms','cms','cms']
        else:
            t=raw_input('输入用 ''户名，密码，数据库名''。注意：都好隔开')
            info=t.split(',')
        try:
            print(info)
            conn=mysql.connector.connect(user=info[0],passwd=info[1],db=info[2])
        except Exception as err:
            print(err)
            exit()
        cur=conn.cursor()
        tablelist=[]
        if ttt<10:
            tables=raw_input('输入表名：')
            tablelist=tables.split(',')
        elif ttt>10:
            cur.execute('show tables')
            re=cur.fetchall()
            for t in re:
                tablelist.append(t[0])
        else:
            print('命令参数错误。')
            exit()
        start(cur,tablelist)
        conn.close()
    except Exception as err:
        with open('xxx.txt',mode='a') as out_err:
                print(str(err))
                print(str(err))
                out_err.write(str(err))
main1()
