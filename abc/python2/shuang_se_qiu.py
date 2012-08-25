# -*- coding: cp936 -*-
def shuang_se_qiu():
    '''双色球！！'''
    import random
    def getRedNum():
        return random.randrange(1,34)
    def getBlueNum():
        return random.randrange(1,16)
    counter=0
    result=[]
    while counter < 6:
        counter+=1
        r=getRedNum()
        result.append(str(r) if not r<10 else '0'+str(r))
    r=getBlueNum()
    r=str(r) if not r<10 else '0'+str(r)
    return [r]+result
