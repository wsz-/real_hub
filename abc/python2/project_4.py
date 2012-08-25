# -*- coding: cp936 -*-
def findPalindromic(n):
    '''找出2个n位数相乘的到得回文数中最大的一个'''
    a=int('1'+'0'*(n-1))
    b=int('1'+'0'*n)
    end=int('1'+'0'*2*(n-1))
    import time
    start=time.clock()
    def get_max_as_str(n):
        result='9'*n
        return str((int)(result)**2)
    num=get_max_as_str(n)
    nex=num
    while nex >end:
        nex=findNextPalindromic(nex)
        #print nex
        for i in range(a,b):
            if nex%i==0 and len(str(nex/i))==n:
                print nex,i,nex/i
                print time.clock()-start
                return None
    return None
def findNextPalindromic(num):
    def to_str(lst):
        result=''
        for i in lst:
            result+=str(i)
        return result
    def cmpp(lst1,lst2):
        lst1=to_str(lst1)
        lst2=to_str(lst2)
        return int(lst1)-int(lst2)
    def cover(lst):
        i=0
        length=len(lst)
        mid=length/2
        while i<mid:
            #print i,mid,lst
            lst[length-i-1]=lst[i]
            i+=1
        return lst
    def getNext(a):
        a=int(a)
        result= 9 if a ==0 else a-1
        return str(result)
    if isinstance(num,int):
        num=list(str(num))
    elif isinstance(num,str):
        num=list(num)
    elif isinstance(num,list):
        pass
    else :
        raise Exception('错误出入')
    '''试着改变左半部分'''
    num_=num[:]
    cover(num_)
    if cmpp(num_,num) < 0:
        return int(to_str(cover(num_)))
    '''试着改变右半部分'''
    length=len(num)
    mid=length/2
    pos=mid-1 if length &1==0 else mid
    while not pos < 0:
        nex=getNext(num[pos])
        if nex > num[pos]:
            num[pos]='9'
            pos-=1
        else:
            num[pos]=nex
            break
    return int(to_str(cover(num)))
