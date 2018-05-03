class Person():
	
	def __init__(self):
		self.__money = 100

	def getMoney(self):
		return self.__money

	def setMoney(self,money):
		if money <= 0:
			print('传入金额有误')
		else:
			self.__money = money

laosun = Person()
laosun.setMoney(500)
print(laosun.getMoney())
