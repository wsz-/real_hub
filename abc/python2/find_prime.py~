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
def mod(a,x,n):
    if x==0:
        return 1
    elif x&1==1:
        return (a*mod(a,x-1,n))%n
    else:
        return square(mod(a,x/2,n))%n
if __name__=='x__main__':
    t=findPrime(10000)
    count=1
    while True:
        z=findPrime2(10000)
        if len(t)!=len(z):
            break
        else:
            count+=1
        if count%(2**5)==0:
            print 1.0/count
    print count
print 'ss'
