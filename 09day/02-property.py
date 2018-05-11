class Money(object):
	def __init__(self):
		self.__money = 0
	@property
	def money(self):
		return self.__money
	
	@money.setter
	def money(self,value):
		if isinstance(value,int):
			self.__money = value

		else:
			print('error:不是整数型数字')

m = Money()
m.money = 5000
print(m.money)
