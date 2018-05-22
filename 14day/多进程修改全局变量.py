import os
import time
rpid = os.fork()

num = 0
if rpid ==0:
	num += 1
	print('我是子进程%d,pid=%d,ppid=%d'%(num,os.getpid(),os.getppid()))

else:
	print('我是父进程%d,pid=%d,ppid=%d'%(num,os.getpid(),os.getppid()))

print('我是哈哈')	
