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
        try:
            con=self.con
        except:
            self.con=mysql.connector.connect(user=self.user,passwd=self.passwd,db=self.db,port=self.port,host=self.host)
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
def create(table_name='bes_mst'):
    db=Xedk()
    tablelist=[table_name]
    re={}#bean 属性名
    colum_name={}#表字段名
    val_type={}#字段类型
    dao_query={}#查询赋值语句
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
        re[table]=[]
        colum_name[table]=[]
        val_type[table]=[]
        try:
            sql='show fields from '+str(table)
            result=db.executeSql(sql)
            for tup in result:
                #print(tup)
                colum_name[table].append(tup[0])
                val_type[table].append(changer[tup[1][0:3]])
                st=t2b(tup[0])
                #tt='private '+changer[tup[1][0:3]]+' ' +st+';'
                re[table].append(st)
                #print(b2t(st))
        except Exception as err:
            print(str(err))
    #print(val_type)
    for item in colum_name[table_name]:
        print(item,end=',')
    print()
    #######################
    ##查询
    #######################
    counter=0;
    dao_query[table_name]=[]
    dao_query_template='''if (null == list.get(%(i)s) || list.get(%(i)s).equals("")) {
		//%(bean_name)s.set%(XXX)s(%(new)s);
	}else{
                %(bean_name)s.set%(XXX)s(%(type_start)slist.get(%(i)s)%(type_end)s);
	}
'''
    for item in re[table_name]:
        data={
            'i':counter,
            'XXX':item[0].upper()+item[1:],
            'new':'""',
            'type_start':'',
            'type_end':'',
            'bean_name':t2b(table_name)+'Bean',
            'class_name':t2b(table_name)[0].upper()+t2b(table_name)[1:]+'Bean'
            }
        if val_type[table_name][counter]!='String':
            data['type_start']='new '+val_type[table_name][counter]+'('
            data['type_end']=')'
            data['new']='new '+val_type[table_name][counter]+'(0)'
        counter+=1
        dao_query[table_name].append(dao_query_template % data)
    #print(dao_query)
    for item in dao_query[table_name]:
        print(item)
    ####################
    ##新增
    ####################
def t2b(t):
    st=''
    up=False
    for i in t.lower():
        if up==True:
            st=st+i.upper()
            up=False
        elif i!='_':
            st=st+i
        else:
            up=True
    return st
def b2t(b):
    st=''
    for i in b:
        if i.isupper():
            st+='_'+i.lower()
        else:
            st+=i
    return st
if __name__=='__main__':
    create('dc_log_new')
