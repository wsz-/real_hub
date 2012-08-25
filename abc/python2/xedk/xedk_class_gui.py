#xedk_class.py
import mysql
import mysql.connector
_Xedk__count=0
class Xedk:
    def __init__(self,user='xedk',passwd='admin',db='xedk',host='127.0.0.1',port=3306):
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
        print('对象销毁。')
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
        self.con=mysql.connector.connect(user=self.user,passwd=self.passwd,db=self.db,port=self.port,host=self.host)
from tkinter import * #@UnusedWildImport
class App:
    def __init__(self):
        tk=Tk()
        tk.geometry("700x400-20+20")
        tk.resizable(width=True,height=True)
        self.frame=Frame(tk)
        self.frame.pack()
        self.lst=[]
        self.swap=''
        self.xedk=Xedk()
        self.button=Button(self.frame,
                           text='Quit',
                           command=self.frame.quit)
        self.hi=Button(self.frame,
                       text='执行',
                       command=self.say_hi)
        self.clear=Button(self.frame,
                          text='清空',
                          command=self.cl)
        self.e=StringVar()
        self.e.set('')
        self.txt=Entry(self.frame,textvariable=self.e,width=80)
        self.txt.pack()
        self.hi.pack(side=RIGHT)
        self.button.pack(side=RIGHT)
        self.clear.pack(side=RIGHT)
        self.textBox=Text(width=200)
        self.textBox.pack()
        self.frame.mainloop()
    def start(self,db,tablelist):
        pass
    def splitResult(self,data):
        try:
            self.swap=[i for i,j in data]
        except:
            self.swap=[i for i in data]
    def say_hi(self):
        tt=self.xedk.executeSql(str(self.e.get()))
        self.splitResult(tt)
        for t in self.swap:
            self.textBox.insert(END,str(t)+'\n')
    def cl(self):
        self.textBox.selection_clear()
        self.textBox.destroy()
        self.creatTextBox()
    def creatTextBox(self):
        self.textBox=Text(width=200)
        self.textBox.pack()
if __name__=='__main__':
    App()
