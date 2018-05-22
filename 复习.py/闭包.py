def test(a,b):
	def test1(i):
	#	print(a*i+b)
		return a+b+i
	return test1
ret = test(1,2)
#ret(2)
print(ret(1))
