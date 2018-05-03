class Father():
	def play(self):
		print('喜欢玩电脑')

class Mother():
	def cook(self):
		print('喜欢做饭')



class Son(Father,Mother):
	def play(self):
		print('喜欢玩手机')
	def cook(self):
		print('喜欢做家务')

xiaoli = Son()
xiaoli.play()
xiaoli.cook()
	
