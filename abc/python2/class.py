class A(object):
    idd='idd'
    def __init__(self,name='sb'):
        self.name=name
    def test(self):
        print self.name
    @staticmethod
    def tt():
        print '123'
    # __slots__=('a','b','name')
import sqlite3
con=sqlite3.connect('d:/mydb.db3')
cur=con.cursor()
try:
    cur.execute('create table if not exists foo(id,name)')
except Exception as e:
    print e
d=cur.execute('select * from foo')
con.commit()
s=d.fetchall()
print d.rowcount
print s
print s
