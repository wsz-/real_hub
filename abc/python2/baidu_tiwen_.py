# -*- coding: cp936 -*-
senList=['����/a','����/a','ѧ/a','��/b','ѧ��/a','��/b','��/c','��/c','��/c','���/a','��ѧ/a']
wordList=['����', '����', '����ѧ', '���ù���', '���ù���ѧ', '����ѧ']
result=[]
wordList=sorted(wordList,key=lambda x:len(x))
weight={'��':0,'��':1,'��':2}
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
