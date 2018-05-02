class Person():
	def __init__(self,name):
		self.name =name
		self.hp = 100
		self.gun = None
	def zhuangzidan(self,danjia,bullet):
		danjia.addBullet(bullet)

	def zhuangdanjia(self,gun,danjia):
		gun.addDanJia(danjia)

	def takeGun(self,gun):
		self.gun =gun

	def openGun(self,diren):
		if diren.hp > 0:
			zidan = self.gun.popGunBullet()
			if zidan:
				zidan.kill(diren)
			else:
				print('没子弹了')



class Gun():
	def __init__(self,name):
		self.name = name
		self.danjia = None
	
	def addDanJia(self,danjia):
		self.danjia = danjia

	def popGunBullet(self):
		return self.danjia.popBullet()

class DanJia():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []

	def addBullet(self,bullet):
		self.bullet_list.append(bullet)

	def popBullet(self):
		if self.bullet_list:
			return self.bullet_list.pop()
		else:  
			return None




class Bullet():
	def __init__(self):
		self.weili = 15

	def kill(self,diren):
		diren.hp -= self.weili
		if diren.hp <= 0:
			diren.hp = 0
			print('%s死了，剩余血量%d'%(diren.name,diren.hp))
		else:
			print('%s剩余血量为:%d'%(diren.name,diren.hp))



	
laowang = Person('老王')
ak47 = Gun('ak47')
danjia = DanJia(30)
for i in range(30):
	bullet = Bullet()
	laowang.zhuangzidan(danjia,bullet)
laowang.zhuangdanjia(ak47,danjia)



laosong = Person('老宋')
laowang.takeGun(ak47)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)




