def find(n=100):
    import time
    start=time.clock()
    a=1
    b=1
    for i in range(1,n+1):
        a+=i**2
        b+=i
    print a-b**2
    print time.clock()-start
