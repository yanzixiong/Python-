class boy():
	def __init__(self,age,height):
		self.age = age
		self.height = height
		self.games = []
		for i in range(3):
			game = input("输入游戏")
			self.games.append(game)
			
	def study(self):
		print('爱学习')
	def drive(self,car):
		print('会开车%s'%car)
	def showage(self,age):
		print('年龄是%d'%age)
	def addgames(self,game):
		self.games.append(game)
	def playgame(self):
		for i in self.games:
			print(i)

yzx = boy(20,175)
yzx.study()
yzx.drive('奔驰')
yzx.showage(10)
yzx.addgames()
yzx.playgame()

huangjie = boy(19,165)
huangjie.study()
huangjie.drive('玛莎拉蒂')
huangjie.showage(19)
huangjie.addgames()
huangjie.playgame()
