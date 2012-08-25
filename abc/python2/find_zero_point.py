# -*- coding: cp936 -*-
def avg(x,y):
    '''求平均值，高精度。'''
    return float(x+y)/2
def func_(x):
    return x*x*x+2*x*x-1
def jie(f,a,b):
    '''解方程f（x）=0。给定f(a)<0 且f(b)>0'''
    #print  (a, b)
    if f(a)<0 and f(b)>0:
        pass
    else:
        raise Exception('给出的猜测值错误,或者此区间有两个或两个以上的解。')
    v=avg(a,b)
    fv=f(v)
    #print(v,fv)
    if -0.000001 < fv < 0.000001:
        print '解：' + str(v)
        return None
    if(fv > 0):
        return jie(f,a,v)
    else:
        return jie(f,v,b)
def abs(n):
    '''求绝对值。'''
    return n if not n<0 else -n
def my_sqrt(n,guess=1.0,e=1e-10):
    '''求平方根。'''
    n*=1.0
    return guess if abs(n-guess*guess) < e else my_sqrt(n,(n/guess+guess)/2,e)
def tui_ce(f,start,end,step):
    '''推测方程的解所在的区间'''
    if start==end:
        raise Exception('区间首尾相接。')
    start=1 if start==None else start
    end=2 if end==None else end
    start=0.1 if step==None else step
    fs=f(start)
    fe=f(end)
    if fs < fe:
        if fs > 0:
            tui_ce(f,start-step,start,step)
        elif fe <0:
            tui_ce(f,fe,end+step,step)
        else:
            return (start,end)
    elif fs==fe:
        tui_ce(f,start,end+step,step)
    else :#fs > fe
        if fe > 0:
            tui_ce(f,end,end+step,step)
        elif fs <0:
            tui_ce(f,start-step,start,step)
        else:
            return (start,end)
def jie_fang_cheng(f,a=-10,b=10):
    '''求解方程。'''
    r=list(tui_ce(f,-1000,1000,0.05))
    while True:
        try:
            jie(f,r[0],r[1])
            print r
        except Exception as err:
            r[1]=r[1]-0.05
            if not r[0] < r[1]:
                print r
                break
