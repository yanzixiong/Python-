class Pizza(object):
	def  prepare(self):#准备披萨
		return 'prepare pizza'
	def bake(self): #烘烤披萨
		return 'bake pizza'
	def cut(self):	#切割披萨
		return 'cut pizza'
	def box(self): #披萨装盒
		return 'box pizza'
# 创建一个披萨店
class PizzaStore(object):
	
	def orderPiaaz(self):#下订单
		self.pizza = Pizza()
		print(self.pizza.prepare())
		print(self.pizza.bake())
		print(self.pizza.cut())
		print(self.pizza.box())

#增加了几种口味
class CheesePizza(object):
	def perpare(self):  #第一种披萨
		return 'prepare Cheese pizza'

	def bake(self):	
		return 'bake Cheese pizza'

	def	cut(self): 
		return 'cut Cheese pizza'
	def box(self):
		return 'box Cheese pizza'

class GreekPizza(object):
	def perpare(self):  #第一种披萨
		return 'prepare Greek pizza'

	def bake(self):	
		return 'bake Greek pizza'

	def	cut(self): 
		return 'cut Greek pizza'
	def box(self):
		return 'box Greek pizza'

class PepperoniPizza(object):
	def perpare(self):  #第一种披萨
		return 'prepare Pepperoni pizza'

	def bake(self):	
		return 'bake Pepperoni pizza'

	def	cut(self): 
		return 'cut Pepperoni pizza'
	def box(self):
		return 'box Pepperoni pizza'

	

		
		

