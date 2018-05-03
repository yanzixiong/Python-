class Father():

	def sport(self):
		print('踢足球')
	def money(self):
		print('双手挣钱')

class Mother():
	def cook(self):
		print('会做饭')
		
	def clear(self):
		print('会洗衣服')

class Girl(Father,Mother):
	pass


xiaohong = Girl()
xiaohong.sport()
xiaohong.money()
xiaohong.cook()
xiaohong.clear()
