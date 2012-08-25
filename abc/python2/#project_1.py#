def addIt(base=0,end=1000,step=3):
    result=base
    while base<=end:
        result+=base
        base+=step
        #print result,base
    return result
def addIt2(end=1000):
    def addAll(x):
        return x*(x+1)/2
    def addAllByBase(base=end,x=0):
        return addAll(base/x)*x
    return addAllByBase(x=3)+addAllByBase(x=5)-addAllByBase(x=15)
def test():
    return addIt()+addIt(step=5)-addIt(step=3*5)
if __name__=="__main__":
    print addIt2(),test()
