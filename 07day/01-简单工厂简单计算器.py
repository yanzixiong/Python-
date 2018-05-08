class OP(object):
	def __init__(self,num1 = 0 ,num2 = 0):
		self.num1 = num1
		self.num2 = num2

	def getResult(self):
		pass


class Jia(OP):
	def getResult(self):
		return self.num1 + self.num2

class Jian(OP):
	def getResult(self):
		return self.num1 - self.num2

class Cheng(OP):
	def getResult(self):
		return self.num1 * self.num2

class Chu(OP):
	def getResult(self):
		if num2 != 0:
			return self.num1 / self.nmu2

class Factory(object):
	def creat_op(self,type):
		if type == '+':
			return Jia()
		elif type == '-':
			return Jian()
		elif type == '*':
			return Cheng()
		elif type == '/':
			return Chu()

fac = Factory()
jia = fac.creat_op('+')
jia.num1 = 2
jia.num2 = 3
print(jia.getResult())
