import mysql
import mysql.connector
import datetime
from string import Template
from sys import argv
#def start():
if 1:
    time=datetime.datetime
    if len(argv)==4:
        try:
            conn=mysql.connector.connect(user=argv[1],passwd=argv[2],db=argv[3])
        except Exception as err:
            print('数据库连接失败！')
            print(str(err))
            exit()
    else:
        conn=mysql.connector.connect(user='cms',passwd='cms',db='xedk')
    cur=conn.cursor()
    tablelist=[]
    if len(argv)==1 or len(argv)==4:
        tables=input('输入表名：')
        start=time.now()
        tablelist=tables.split(',')
    elif argv[1].lower()=='all':
        cur.execute('show tables')
        re=cur.fetchall()
        for t in re:
            tablelist.append(t[0])
    else:
        print('命令参数错误。')
        exit()
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
                    print(tt,file=out)
        except Exception as err:
            with open('xxx.txt',mode='a') as out_err:
                print(str(err),file=out_err)
    conn.close()
    end=time.now()
    print(end-start)
