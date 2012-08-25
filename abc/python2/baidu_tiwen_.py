# -*- coding: cp936 -*-
senList=['经济/a','管理/a','学/a','在/b','学科/a','上/b','从/c','属/c','于/c','社会/a','科学/a']
wordList=['属于', '从属', '管理学', '经济管理', '经济管理学', '社会科学']
result=[]
wordList=sorted(wordList,key=lambda x:len(x))
weight={'从':0,'属':1,'于':2}
def b2dict(lst):
    dic={'a':[],'b':[],'c':[]}
    for item in lst:
        dic[item[-1]].append(item[:-2])
    return dic
def compose(senDic,wordList,mark):
    result=[]
    for index in range(len(wordList)-1,0,-1):
        if senDic[mark]==[]:
            break
        else:
            if findWord(wordList[index],senDic[mark]):
                result.append(wordList[index])
    return result
def findWord(st,lst,src='',result=''):
    findit=False
    if src=='':
        src=st
    #print('start:'+src+' '+result)
    if st=='':
        return True
    index=0
    for item in lst:
        length=len(item)
        if item==st[0:length]:
            result+=item
            del lst[index]
            findit=findWord(st[length:],lst,src=src,result=result)
            break
        index+=1
    return findit
senDic=b2dict(senList)
a=compose(senDic,wordList,'a')
c=compose(senDic,wordList,'c')
print(a,c,senDic)
