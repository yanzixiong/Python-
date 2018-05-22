from threading import Thread
import time
import threading

def work():
	name = threading.current_thread().name
	print(name)
	num = 1
	num+=1
	print('哈哈%d'%num)

def work1():
	name = threading.current_thread().name
	print(name)
	num = 100
	print('呵呵呵%d'%num)


t = Thread(target=work)		
t.start()

t1 = Thread(target=work1)
t1.start()
