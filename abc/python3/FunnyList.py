class FunnyList(object):
    def __init__(self,start=1,step=1):
        self.changed={}
        self.counter={}
        self.step=step
        self.start=start
    def __len__(self):
        raise Exception()
    def __getitem__(self,key):
        try:
            return self.__changed[key]
        except:
            return self.__start+self.__step*key
    def __setitem__(self,key,value):
        try :
            self.counter[key]+=1
        except:
            self.counter[key]=1
            self.changed[key]=value
    def popLeft(self):
        mins=self.changed.keys()[0]
        for key in self.changed.keys():
            if key > mins:
                mins=key
        return self.changed[mins]
    def popRight(self):
        maxs=self.changed.keys()[0]
        for key in self.changed.keys():
            if key < maxs:
                maxs=key
        return self.changed[maxs]
