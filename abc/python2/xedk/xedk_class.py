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
