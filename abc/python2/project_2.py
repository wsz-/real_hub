def test(ma=4000000):
    fib=[0,1]
    counter=0
    result=0
    while fib[1]<ma:
        tmp=fib[0]
        fib[0]=fib[1]
        fib[1]=fib[1]+tmp
        counter+=1
        if counter%3==0:
            result+=fib[0]
            #print fib[0]
    return result
if __name__=="__main__":
    print test()
