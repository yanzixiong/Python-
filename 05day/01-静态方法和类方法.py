class Dog():
	count = 1
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return '%s我爱你'%self.name



	@classmethod
	def test(cls):
		return cls.count
	




taidi = Dog('泰迪')	
print(taidi)
print(taidi.test())
