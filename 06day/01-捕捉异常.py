try:
	print(yzx)
	open('1.txt')

except (NameError,FileNotFoundError):

	print('出错了')

except Exception as result:
	print('出错了',result)

else:
	print('没有错误')

finally:
	print('大错特错特大错')

print('你怕是个傻子吧')	
