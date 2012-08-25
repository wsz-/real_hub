def check(state,nextX):
    nextY=len(state)
    for i in range(nextY):
        if state[i]-nextX in (0,nextX-i):
            return True
    return False
def queens(state,num):
    if num-1==len(state):
        for pos in range(num):
            if not check(state,pos):
                yield pos
    else:
        for pos in range(num):
            for result in queens(state,num):
                if not check(result,pos):
                    yield (pos,)+result
#lt=[1,3,2]
#print(list(queens(lt,4)))
print(list(queens((),4)))
