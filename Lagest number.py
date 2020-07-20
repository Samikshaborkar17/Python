Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = float(input('Enter the first number: '))
Enter the first number: 6
>>> num2 = float(input('Enter the second number: '))
Enter the second number: 7
>>> num3 = float(input('Enter the third number: '))
Enter the third number: 8
>>> if(num1>num2) and (num1>num3):
	print(num1,'is largest of all the three numbers')
elif(num2>num1) and (num2>num3):
	print(num2,'is largest of all the three numbers')
else:
	print(num3,'is largest of all the three numbers')

	
8.0 is largest of all the three numbers
>>> 