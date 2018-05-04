class SweetPotato():
	
	def __init__(self):

		self.cooklevel = 0#烤的等级

		self.cookstr = '生的'

		self.condliments = [] #作料

	def __str__(self):

		return self.cookstr+str(self.condliments)

	def cook(self,time):

		self.cooklevel+=time

		if self.cooklevel > 0 and self.cooklevel < 3:

			self.cookstr = "半生不熟"

		elif self.cooklevel>=3 and self.cooklevel <6:

			self.cookstr = "熟了"

		elif self.cooklevel >=6:

			self.cookstr = "糊吧了"

	def addcondliment(self,item):

		self.condliments.append(item)

sp = SweetPotato()

sp.cook(1)

sp.addcondliment("盐")

print(sp)

sp.cook(1)

sp.addcondliment("芥末")

print(sp)

	

sp.cook(1)

sp.addcondliment("酱油")

print(sp)

	

sp.cook(1)

print(sp)

	

sp.cook(1)

print(sp)	

sp.cook(1)

sp.addcondliment("老抽")

print(sp)
