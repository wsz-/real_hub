import tt
@tt.ttn
def makeP_shou(x):
    P=[2]
    p=[2]
    n=3
    while n < x:
        for i in p:
            if n%i==0:
                break
        else:
            P.append(n)
        n+=2
        while n>p[-1]**2:
            p.append(P[len(p)])
    return 
@tt.ttn
def makeP(x):
    p=[2]
    n=3
    flag=False
    while n < x:
        print n
        for i in p:
            print 'i:',i
            if n<i**2:
                flag=False
                break
            if n%i==0:
                print n
                flag=True
                break
        if flag:
            p.append(n)
        n+=2
    return p
