# -*- coding: cp936 -*-
def tt(*args,**karg):
    '''请注意，我这个名字 tt ，绝对不是套套的意思，请不要想歪了。
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
                print 'SB了吧，用了这么久！',time,'秒'
                print ' --! '
                if not over_:
                    print '还没有算完啊，骚年'
            else:
                print '勇士！你赢了！伟大的勇士啊！',time,'秒'
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
        print clock()-start,'秒'
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
