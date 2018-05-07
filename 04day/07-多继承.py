class A():
	def testA(self):
		print('------LOVE----')
	def test(self):
		print('哈哈')
class B():

	def testB(self):
		print('-----Big----')
	def test(self):
		print('嘿嘿')

class C(A,B):
	pass



c = C()
c.testA()
c.testB()
c.test()
