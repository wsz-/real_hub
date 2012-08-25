# -*- coding: cp936 -*-
def findPrime(n=100):
    start=1
    result=[]
    while start<=n:
        if isPrime(start):
            result.append(start)
        start+=2
    return result
def findPrime2(n=100):
    start=1
    result=[]
    while start<=n:
        if isPrime2(start):
            result.append(start)
        start+=2
    return result
def isPrime(x,ma=60):
    if x==0 or x==1:
        return False
    i=1
    ma=x**(1.0/2)
    while i<ma:
        i+=1
        if x%i==0:
            return False
    return True
def square(x):
    return x*x
def isPrime2(n=10,a=3):
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
    is_prime=test(n,40)
    return is_prime
def find(nth):
    import time
    start=time.clock()
    i=1
    num=1
    while True:
        num+=2
        if isPrime(num):
            i+=1
            if i==nth:
                print num,i,'  ',time.clock()-start
                break
