import os
tipe = os.fork()

if tipe ==0:
	print('我是子进程%d,pid=%d,ppid=%d'%(tipe,os.getpid(),os.getppid()))

else:
	print('我是父进程%d,pid=%d,ppid=%d'%(tipe,os.getpid(),os.getppid()))
