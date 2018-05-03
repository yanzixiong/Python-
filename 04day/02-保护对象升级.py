class Person():
	
	def __init__(self,money):
		self.__money = money

	def getMoney(self):
		return self.__money

	def setMoney(self,money):
		if money <= 0:
			print('传入金额有误')
		else:
			self.__money = money

laosun = Person(100)
laosun.setMoney(500)
print(laosun.getMoney())
