Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input('enter a number: '))
enter a number: 73
>>> for i in range(2,num):
	if(num%i)==0:
		print(num,'is not a prime number')
	else:
		print(num,'is a prime number')
		break
	if(num==1):
		print('the number is a prime number')

		
73 is a prime number
>>> 