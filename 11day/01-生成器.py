def fib():
	i = 0
	a,b = 0,1
	while i < 5:
		print(b)
		a,b = b,a+b
		i += 1
fib()

