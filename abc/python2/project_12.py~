def findPrime(n=100):
    start=1
    result=[]
    if n>1:
        result.append(2)
    while start<=n:
        if isPrime(start):
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
def find(n):
    src=findPrime(n)
    lst=range(1,n)
    result=[]
    for i in lst:
        result=concat(result,find_factor(i,src))
    return result
def concat(a,b):
    x=sorted(a)
    y=sorted(b)
    if len(a)> len(b):
        x=b
        y=a
    result=[]
    dx={}
    dy={}
    for i in x:
        dx[i]=x.count(i)
    for i in y:
        dy[i]=y.count(i)
    table={}
    for k,v in dx.items():
        table[k]=v
    for k,v in dy.items():
        if v > table.setdefault(k,0):
            table[k]=v
    for k,v in table.items():
        result.extend([k]*v)
    return result
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
        if n<lst[i]:
            break
    return result
def x(n):
    import time
    start=time.clock()
    lst=find(n)
    #print lst
    result=1
    for i in lst:
        result*=i
    print result
    print time.clock()-start
gcd=lambda x,y:y==0 and x or gcd(y,x%y)
def lcm(x):
    import time
    start=time.clock()
    num=1
    for i in range(1,x+1):
        #print "%15s" % num,gcd(num,i),i
        num*=i/gcd(num,i)
    print time.clock()-start
    return num
