class Person(object):
	def __init__(self,name,age):
		print('__init__')
		self.name = name
		self.age = age
p = Person('laowang',33)
print(p)
