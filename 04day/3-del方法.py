class Dog():
	
	def eat(self):
		print('吃')

	def run(self):
		print('跑')

	def __del__(self):
		print('def方法')

taidi = Dog()
hashiqi = taidi
taidi.eat()
taidi.run()
'''
del taidi
print('哈哈哈')
'''


del hashiqi
del taidi
print('呵呵呵')
