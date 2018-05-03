class Dog():

	def __init__(self):
		self.name = '哈士奇'
	
	def __str__(self):
		return self.name

	def __del__(self):
		print('del方法')



taidi = Dog()
hashiqi = taidi
print(taidi)
#del taidi
del hashiqi

print('呵呵呵呵呵')



class Dog():

	def __init__(self,name):
		self.name = name
	
	def __str__(self):
		return '我爱你'

	def __del__(self):
		print('del方法')



taidi = Dog('泰迪')
hashiqi = taidi
print(taidi)
del taidi
del hashiqi

print('呵呵呵呵呵')
