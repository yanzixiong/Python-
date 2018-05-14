class Person(object):
	def __new__(cls,name,age):
		print('__new__')
		instance = object.__new__(cls)
		return instance

	def __init__(self,name,age):
		print('__init__')
		self.name = name
		self.age = age

p = Person('laowang',33)
print(p.name)
print(p.age)
