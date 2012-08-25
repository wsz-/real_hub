'''
Created on Jun 25, 2012

@author: Sam
'''
from Tkinter import * #@UnusedWildImport
class App:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        self.xedk=Xedk()
        self.button=Button(frame,
                           text='Quit',
                           command=frame.quit)
        self.hi=Button(frame,
                       text='转换',
                       command=self.say_hi)
        self.clear=Button(frame,
                          text='清空',
                          command=self.cl)
        self.e=StringVar()
        self.e.set('')
        self.txt=Entry(frame,textvariable=self.e)
        self.txt.pack()
        self.hi.pack(side=RIGHT)
        self.button.pack(side=RIGHT)
        self.clear.pack(side=RIGHT)
        self.textBox=Text()
        self.textBox.pack()
    def start(self,db,tablelist):
        '''
        
        :param db:
        :param tablelist:
        '''
        print(tablelist)
        import datetime
        time=datetime.datetime
        re=[]
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
                result=db.executeSql(sql)
                re.append('表：'+table) 
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
                    re.append(tt)
            except Exception as err:
                print(str(err))
        end=time.now()
        re.append(end-start)
        return re
    def say_hi(self):
        tablelist=[]
        tablelist.append(self.e.get())
        result=self.start(self.xedk,tablelist)
        for tt in result:
            self.textBox.insert(END,str(tt)+'\n')
    def cl(self):
        self.textBox.selection_clear()
        self.textBox.destroy()
        self.creatTextBox()
    def creatTextBox(self):
        self.textBox=Text()
        self.textBox.pack()
        
_Xedk__count=0
class Xedk:
    def __init__(self,user='xedk',passwd='admin',db='xedk',host='127.0.0.1',port=3306):
        import mysql.connector
        self.user=user
        self.passwd=passwd
        self.db=db
        self.host=host
        self.port=port
        global __count
        __count+=1
        print('有',__count,'个链接。')
        self.con=mysql.connector.connect(user=self.user,passwd=self.passwd,db=self.db,port=self.port,host=self.host)
    def __del__(self):
        self.close()
        del self
        print('数据库对象销毁。')
    def getMysqlCon(self):
        return self.con
    def executeSql(self,sql):
        try:
            con=self.getMysqlCon()
            self.cur=con.cursor()
            self.cur.execute(sql)
            t=self.cur.fetchall()
            con.commit()
        except Exception as err:
            print(str(err))
        return t
    def close(self):
        self.con.close()
        global __count
        __count-=1
        print('连接关闭。还剩',__count,'个连接。')
    def openCon(self):
        import mysql.connector
        self.con=mysql.connector.connect(user=self.user,passwd=self.passwd,db=self.db,port=self.port,host=self.host)

if __name__ == '__main__':
    root=Tk()
    root.geometry('600x400+100+100')
    app=App(root)
    tt=Xedk().executeSql("show tables")
    app.lst=tt;
    print(str(tt))
    root.mainloop()
