# -*- coding: cp936 -*-
def isPrime(n=10):
    if n==0 or n==1:
        return False
    is_prime=True
    def test(n,times):
        import random
        for i in range(times):
            t=random.randrange(n)
            while t<1:
                t=random.randrange(n) 
            tmp=mod(t,n-1,n)
            if tmp!=1:
                return False
        return True
    is_prime=test(n,40)#做66次测试，只为心安理得 --！
    return is_prime
def mod(a,x,n):
    def square(x):
        return x**2
    if x==0:
        return 1
    elif x&1==1:
        return (a*mod(a,x-1,n))%n
    else:
        return square(mod(a,x/2,n))%n
def findLtPrime(num):
    if num==3:
        return 2
    if num&1==0:
        num-=1
        if isPrime(num):
            return num
    while num>1:
        num-=2
        if isPrime(num):
            return num
def find(num):
    import time
    start=time.clock()
    i=2
    nextNum=num/i
    if num%nextNum==0 and isPrime(nextNum):
            print nextNum
            return None
    while nextNum>1:
        print nextNum
        nextNum=findLtPrime(nextNum)
        if num%nextNum==0:
            print nextNum
            break
    print time.clock()-start
def find_(num):
    import time
    start_time=time.clock()
    end=num/2
    i=1
    while i< num**0.5:
        i+=2
        if num%i==0:
            if isPrime(num/i):
                print num/i
                break
            else :
                num/=i
    print time.clock()-start_time
import math
def factor(x,mi=2):
    temp=mi
    end=math.sqrt(x)+1
    while temp<end:
        if x%temp ==0:
            return temp
        else:
            temp+=1
    return 1
n=600851475143
i=3
import time
start_time=time.clock()
while i<=int(math.sqrt(n))+1:
    if n%i==0:
        if factor(n/i)==1:
            break
        else:
            n/=i
    i+=2
print n/i,n,i
print time.clock()-start_time
