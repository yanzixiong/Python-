def test1():
	while True:
		print('hahahaha')
		yield None
		

def test2():
	while True:
		print('hehehe')
		yield None


t1 = test1()
t2 = test2()

while True:
	t1.__next__()
	t2.__next__()
