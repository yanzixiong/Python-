class Father(object):
		
	def __init__(self,name):
		self.__getgirl = 5
		self.name = name	
	def getGirl(self):
		return self.__getgirl

	def getmoney(self):
		print('%s会挣人民币'%self.name)

	def sport(self):
		print('%s会踢足球'%self.name)

	def __girl(self):
		print('泡妞秘籍')
	
	def askgirl(self):
		self.__girl()




class Son(Father):
	pass	

xiaoming = Son('小明')
print(xiaoming.getGirl())
xiaoming.getmoney()
xiaoming.sport()
xiaoming.askgirl()
