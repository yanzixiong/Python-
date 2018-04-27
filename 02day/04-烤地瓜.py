class muttom():
	def __int__(self):
		self.firelever = 0
		self.firestr = '生的'
		self.condliments = []
	def __str__(self):
		return self.firestr+str(self.condliments)
	def fire(self,time):
		self.firelever += time
		if self.firelever >0 and self.firelever <3:
			self.firestr = '三分熟，还不能吃'
		elif self.firelever >=3 and self.firelever < 5:
			self.firestr = '五分熟，再等等'
		elif self.firelever >=5 and self.firelever <8:
			self.firestr = '火候刚刚好，可以开吃了'
		else:
			self.firestr = '烤焦了,下次注意把控时间'
	def addcondiment(self,condiments):
		self.condiments.append(condiments)
		
hali = muttom()
hali.fire(1)
hali.addcondiment('孜然')
print(hali)
hali.fire(1)
hali.addcondiment('辣椒')
print(hali)
hali.fire(1)
hali.addcondiment('芥末')
print(hali)
hali.fire(1)
hali.addcondiment('胡椒粉')
print(hali)
hali.fire(1)
hali.addcondiment('盐')
print(hali)
