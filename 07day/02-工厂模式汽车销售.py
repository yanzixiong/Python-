class Carstore(object):
	def createcar(self,name):
		pass

	def order(self,name): #制作一个订单
		self.car = self.createcar(name)
		self.car.move()
		self.car.stop()

class DaZhongstore(Carstore):
	def createcar(self,name):
		self.carFactory = CarFactory()
		return self.carFactory.createcar(name)

class PaSaTeCar(object):
	def move(self):
		print('-----车在跑-----')

	def stop(self):
		print('-----停车-----')


class MaiTengCar(object):
	def move(self):
		print('-----车在飞快地跑-----')

	def stop(self):
		print('----立刻停车-----')


class CarFactory(object):
	def createcar(self,name):
		self.name =name 
		if self.name == '帕萨特':
			self.car = PaSaTeCar()

		elif self.name == '迈腾':
			self.car = MaiTengCar()


		return self.car


pasate = DaZhongstore()
pasate.order('帕萨特')


maiteng = DaZhongstore()
maiteng.order('迈腾')


