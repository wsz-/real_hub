import random
import datetime
time=datetime.datetime
lst=[random.choice(range(i)) for i in range(3,1432)]
def sort(lst=[]):
    return lst if len(lst)==0 or len(lst)==1 else sort([i for i in lst[1:] if i > lst[0]])+[lst[0]]+sort([i for i in lst[1:] if i <= lst[0]])
def testSort(lst=lst):
    for i in range(6):
        lst.extend(lst)
    start=time.now()
    result=sort(lst)
    print('排序'+str(len(lst))+'个数字。')
    print(time.now()-start)
