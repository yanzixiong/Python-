class Money(object):
	def __init__(self):
		self.__money = 0
	

	def getMoney(self):
		return self.__money

	def setMoney(self,value):
		if isinstance(value,int):
			self.__money = value
		else:
			print('error:不是整数型数字')

	money = property(getMoney,setMoney)


m = Money()
m.money = 100
print(m.money)
