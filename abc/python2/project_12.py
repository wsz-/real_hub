def findPrime(n=100):
    start=1
    result=[]
    if n>1:
        result.append(2)
    cc=1
    while start<n:
        if isPrime(start):
            cc+=1
            result.append(start)
        start+=2
    return result
def isPrime(x):
    if x==0 or x==1:
        return False
    if x==2:
        return True
    i=1
    ma=x**(1.0/2)
    while i<ma:
        i+=1
        if x%i==0:
            return False
    return True
def square(x):
    return x*x
def find_factor(n,lst):
    def inList(x):
        return lst.count(x)>0
    result=[]
    i=0
    end=len(lst)
    while i<end:
        if n%lst[i]==0:
            n/=lst[i]
            result.append(lst[i])
        else:
            i+=1
        try:
            if n<lst[i]:
                break
        except:
            break
    return result
addAll=lambda x:x*(x+1)/2
def comp(lst):
    result=set()
    n=len(lst)
    cc=1
    while cc<n:
        cc+=1
    return result
def find(n):
    cc=0
    while cc<n:
        a=addAll(i)
        lst=findPrime(i)
        length=len(lst)
        if length>=6
    print find_factor(a,lst),a,lst
