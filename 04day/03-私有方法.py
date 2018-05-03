class Msg():
	
	def __sendMsg(self,money):
		money -= 1
		print('扣钱成功，发送短信')
		
	def publicsend(self,money):
		if money <= 0:
			print('发送失败')
		else:
			self.__sendMsg(money)

msg = Msg()

msg.publicsend(10)

