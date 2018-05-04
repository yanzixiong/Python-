class DateTest():
	def __init__(self,year,month,day):
		self.year = year
		self.month =month
		self.day = day
	def getDate(self):
		print('%s年%s月%s日'%(self.year,self.month,self.day))

	@classmethod	
	def Date(cls,date):
		a,b,c = date.split('-')

		d = cls(a,b,c)
		return d


a = 2018
b = 5
c = 4
d = DateTest(a,b,c)
d.getDate()

str = '2018-05-04'
a,b,c = str.split('-')
d = DateTest(a,b,c)
d.getDate()

str = '2008-08-08'
d.Date(str)
d.getDate()



