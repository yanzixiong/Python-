class Person(object):
	__instance = None
	__init_flag = False
	def __new__(cls,name,age):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance

	def __init__(self,name,age):
		if Person.__init_flag == False:
			self.name = name
			self.age = age
			Person.__init_flag = True

p1 = Person('laowang',33)
p2 = Person('laozhang',30)

print(p1.name)
print(p2.name)
print(id(p1))
print(id(p2))
