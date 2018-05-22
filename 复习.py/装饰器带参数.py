def w2(p):
	def w1(fun):
		def inner():
			if p == 'haha':
				print('验证哈哈')
			elif p == 'hehe':
				print('验证呵呵')

				ret = fun()
				return ret
		return inner
	return w1

@w2('haha')
def test():
	print('哈哈')

@w2('hehe')
def test1():
	print('呵呵')

test()
test1()
				
			
