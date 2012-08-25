class Fun(object):
    def __init__(self):
        self.values=[]
    def add(self,e):
        self.values.append(e)
        self.values.sort()
    def popLeft(self):
        return self.values[0]
    def popRight(self):
        return self.values[-1]
