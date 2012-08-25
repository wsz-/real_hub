class Kj(object):
	def __init__(self):
		self.n=[0]*5
		self.n[0]=3*4
		self.n[1]=self.n[0]*5/4+1
		self.step=4*4
		self.findIt=False;
	def add(self):
		if self.findIt:
			return self.n
		self.n[0]=self.n[0]+self.step
		for i in range(5):
			if i ==0 :pass
			else:
				self.n[i]=self.n[i-1]*5/4
				if not self.check(i):
					break
				if i ==5:
					self.findIt=True
		if not self.findIt:
								return self.add()
	def check(self,i):
		return self.n[i]%4==0
