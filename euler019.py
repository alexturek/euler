class calendar:
	_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	@staticmethod
	def days_in_month(month, year):
		ans = calendar._days[month-1]
		if ans == 28 and calendar.days_in_year(year) == 366:
			ans = 29
		return ans

	@staticmethod
	def days_in_year(year):
		lastdigits = int(str(year)[2:])
		if year % 400 == 0 or (lastdigits != 0 and lastdigits % 4 == 0):
			return 366
		else:
			return 365

	@staticmethod
	def day_of_week(day,month,year):
		# 1/1/1900 was a monday
		incr = 1
		if year < 1900:
			incr = -1
		days = 2 # sunday = 1, monday = 2, ...

		# add days from each year
		for y in range(1900,year,incr):
			#print('adding',incr * calendar.days_in_year(year))
			days = days + incr * calendar.days_in_year(y)
		# add days from each month
		for m in range(1,month):
			#print('adding',calendar.days_in_month(m, year))
			days = days + calendar.days_in_month(m, year)
		# add days from day
		days = days + day - 2
		return (days % 7) + 1

def sundays_first_of_month(year):
	ans = 0
	for y in range(1901,year+1):
		for m in range(1,13):
			if calendar.day_of_week(1,m,y) == 1:
				ans = ans + 1
	return ans

ans = sundays_first_of_month(2000)
