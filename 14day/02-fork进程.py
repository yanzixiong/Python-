from multiprocessing import Process
import os
import time
def test(arg):
	time.sleep(3)
	print('子进程%s，pid=%d'%(arg,os.getpid()))

p = Process(target=test,args=('laowang',))
p.start()

p.join()
print('哈哈哈哈哈哈')

