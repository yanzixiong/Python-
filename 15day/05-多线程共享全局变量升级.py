from threading import Thread,Lock
import time
import threading
g_num =0
def work():
	global g_num
	mutex.acquire()
	for i in range(1000000):
		g_num += 1
	print('%s----%d'%(threading.current_thread().name,g_num))
	mutex.release()


def work1():
	global g_num
	mutex.acquire()
	for i in range(1000000):
		g_num += 1
	print('%s----%d'%(threading.current_thread().name,g_num))
	mutex.release()

t = Thread(target = work)
t1 = Thread(target = work1)

mutex = Lock()

t.start()
t1.start()

	
