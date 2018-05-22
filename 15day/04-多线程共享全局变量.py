from threading import Thread
import time
import threading

g_num = 100
def work():
	global g_num
	g_num += 1
	time.sleep(1)
	print('%s----%d'%(threading.current_thread().name,g_num))

def work1():
	
	global g_num
	print('%s----%d'%(threading.current_thread().name,g_num))


t = Thread(target = work)
t1 = Thread(target = work1)

t.start()
t1.start()

	
