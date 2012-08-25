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
            print('��'+table)
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
    ��������mysql��
    ѡ��ģʽ��
    1.����xedk��ָ����
    11.����xedk�����б���ֶ�
    2.����cms��ָ����
    22.����cms�����б���ֶ�
    3.�ֶ������û��������룬���ݿ⡣ָ����
    33.�������ݿ⣬���������б���ֶ�
    ''');
        else:
            print('����Ҫ������');
            exit()
        ttt=int(ttt)
        if ttt==1 or ttt==11:
            info=['xedk','admin','xedk']
        elif ttt==2 or ttt==22:
            info=['cms','cms','cms']
        else:
            t=raw_input('������ ''���������룬���ݿ���''��ע�⣺���ø���')
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
            tables=raw_input('���������')
            tablelist=tables.split(',')
        elif ttt>10:
            cur.execute('show tables')
            re=cur.fetchall()
            for t in re:
                tablelist.append(t[0])
        else:
            print('�����������')
            exit()
        start(cur,tablelist)
        conn.close()
    except Exception as err:
        with open('xxx.txt',mode='a') as out_err:
                print(str(err))
                print(str(err))
                out_err.write(str(err))
main1()
