square=lambda x:x*x
isEven=lambda x:x&1==0
def n_pow(x=2,y=100):
    return x*n_pow(x,y-1) if y!=0 else 0
def my_pow(x=2,y=100):
    if y==0:
        return 1
    elif y==1:
        return x
    else :
        if isEven(y):
            return square(my_pow(x,y//2))
        else:
            return x*square(my_pow(x,(y-1)//2))
def my_pow1(x=2,y=100):
    result=1;
    while y!=0:
        if y&1==1:
            result*=x
        if y==1:
            break
        x=square(x)
        y=y>>1
        #print x
    return result
def my_pow2(x=2,y=100):
    result=1.0;
    x*=1.0
    while y!=0:
        if y&1==1:
            result*=x
        if y==1:
            break
        x*=x
        y=y>>1
    return result
def p():
    return pow(2.0,100.0)
def p1():
    return 2.0 ** 100
def p2(a=2,b=100):
    bi=[]
    while b!=0:
        bi.append(b%2)
        b /=2
    bi.reverse()
    out=1
    for i in bi:
        out *=out
        if i==1:
            out*=a
    return out
import timeit
#t=timeit.Timer(n_pow)
t0=timeit.Timer(my_pow)
t1=timeit.Timer(my_pow1)
t2=timeit.Timer(my_pow2)
t3=timeit.Timer(p2)
#print t.timeit()
'''
38.1614877814
8.03077347442
5.90630646948
4.44541762652
3.45339675248

3.89466081755
2.7482541762
2.06441220225
1.7876509306
'''
print t0.timeit()
print t1.timeit()
print t2.timeit()
print t3.timeit()
