class Home():
	def __init__(self,area):
		self.area = area #房间剩余的可用面积
		#self.light = '灯是开着的' #灯默认是亮的
		self.containsitem = []
		self.dengs =[]

	def __str__(self):
		msg = '当前房间可用面积为:'+str(self.area)
		if len(self.containsitem) > 0:
			msg = msg + '容纳的物品有'
			for temp in self.containsitem:
				msg = msg +temp.getName()
			msg = msg.strip()
		return msg


	def accommodateitem(self,item):
		#如果可用面积大于物品的占用面积
		needarea = item.getusedarea()
		if self.area > needarea:
			self.containsitem.append(item)
			self.area -= needarea
			print('ok,已经存放到房间中')
		else:
			print('err,房间可用面积为%d，但是当前要存放的物品需要的面积为%d'%(self.area,needarea))

	def addLight(self,light):
		self.dengs.append(light)

	def swith(self)；
		self.degns[0].open()


class Bed():
	def __init__(self,area,name = '床'):
		self.name = name 
		self.area = area
	
	def __str__(self):
		msg = '床的面积为:'+str(self.area)
		return msg


	def getusedarea(self):
		return self.area
	
	def getName(self):
		return self.name

class Light():
		
	def __init__(self,name):
		self.name = name 
		self.isopen = False
	
	def __str__(self):
		msg = '我叫%s灯'%self.name
		return msg 
	
	def open(self):
		self.isopen = True
		print('灯亮了')
	def close(self):
		self.isopen = False
		print('灯灭了')

newHome = Home(100)	
print(newHome)


newBed = Bed(20)
print(newBed)

benladeng = Light('本拉登')
print(benladeng)

newHome.accommodateitem(newBed)
print(newHome)


newBed2 = Bed(30,'席梦思')
print(newBed2)


newHome.accommodateitem(newBed2)
print(newHome)
