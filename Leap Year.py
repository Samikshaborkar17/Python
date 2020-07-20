Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> year = int(input('Enter the year: '))
Enter the year: 2019
>>> if(year%4)== 0:
	if(year%100)== 0:
		if(year%400)== 0:
			print(year,'is a leap year')
		else:
			print(year,'is not a leap year')
	else:
		print(year,'is not a leap year')
else:
	print(year,'is not a leap year')

	
2019 is not a leap year
>>> 