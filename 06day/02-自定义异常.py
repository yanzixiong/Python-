class ShowError(Exception):
	def __init__(self,len,leastlen):
		self.len = len 
		self.leastlen = leastlen

def main():
	try:
		s = input('请输入数字')
		if len(s) < 3:
			raise ShowError(len(s),3)
	except Exception as ret:
		print('捕捉到错误')
		print('输入的是%d位,至少需要%d位'%(ret.len,ret.leastlen))
	else:
		print('没有错误')

main()		
		
