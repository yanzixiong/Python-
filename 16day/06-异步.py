from multiprocessing import Pool
import time
import threading
def test1():
	for i in range(3):
		print('哈哈')
		time.sleep(1)
	return 'hahahahaha'	

def test2():
	print('嘎嘎嘎嘎')

p = Pool(3)
p.apply_async(func=test1,callback=test2)

p.start()
