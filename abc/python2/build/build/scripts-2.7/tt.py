# -*- coding: cp936 -*-
def tt(*args,**karg):
    '''��ע�⣬��������� tt �����Բ������׵���˼���벻Ҫ�����ˡ�
'''
    try:
        cc=args[0]
    except:
        cc=1
    def wrapper(func):
        def new_func(*a,**k):
            from time import clock
            start=clock()
            over_=True
            for i in range(cc-1):
                if clock()>1:
                    over_=False
                    break
                func(*a,**k)
            result=func(*a,**k)
            time= clock()-start
            if time >0.5:
                print 'SB�˰ɣ�������ô�ã�',time,'��'
                print ' --! '
                if not over_:
                    print '��û�����갡��ɧ��'
            else:
                print '��ʿ����Ӯ�ˣ�ΰ�����ʿ����',time,'��'
            return result
        new_func.__doc__='SB'
        return new_func
    return wrapper
def ttn(func):
    def wrapper(*a,**k):
        from time import clock
        start=clock()
        #print a,k
        v= func(*a,**k)
        print clock()-start,'��'
        return v
    return wrapper
@ttn
def test(ma=400):
    fib=[0,1]
    counter=0
    result=0
    while fib[1]<ma:
        tmp=fib[0]
        fib[0]=fib[1]
        fib[1]=fib[1]+tmp
        counter+=1
        if counter%3==0:
            result+=fib[0]
            #print fib[0]
    return result
if __name__=="__main__":
    print test(10)
