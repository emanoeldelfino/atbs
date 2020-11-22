import re

# DD/MM/YYYY

dateRegex = re.compile(r'''
	(3[01]|[12]\d|0[1-9]) # day
	(/|-|\.)              # sep
	(1[0-2]|0[1-9])       # month
	(/|-|\.)              # sep
	([12]\d\d\d)          # year
	''', re.VERBOSE)

dates = ['29.02.2019', '30-02-2993', '15/07/2019', '01-12-2999']

for date in dates:
	mo = dateRegex.search(date)

	day = mo.group(1)
	month = mo.group(3)
	year = int(mo.group(5))

	print(f'Date {day} {month} {year} is ', end='')

	if month in ['04', '06', '09', '11'] and int(day) > 30 or month != '02' and int(day) > 31:
		print('incorrect.')
	elif month == '02':
		# leap year check
		check = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
		if int(day) > check:
			print('incorrect.')
		else:
			print('correct.')
	else:
		print('correct.')
