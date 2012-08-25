class A(object):
    def __init__(self,name='sb'):
        self.name=name
    def test(self):
        print self.name
    @staticmethod
    def tt():
        print '123'
    __slots__=('a','b','name')
a=A()
a.w=1
