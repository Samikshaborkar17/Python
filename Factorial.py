Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input('Enter the number: '))
Enter the number: 7
>>> factorial = 1
>>> if num<0:
	print('Please enter a non negative number')
elif num==0:
	print('The factorial of 0 are 0 and 1')
else:
	for i in range(1,num+1):
		factorial=factorial*i
		break
	print(factorial)

	
1
>>> num = 7
>>> factorial = 1
>>> if num<0:
	print('Please enter a non negative number')
elif num==0:
	print('The factorial of 0 are 0 and 1')
else:
	for i in range(1,num+1):
		factorial=factorial*i
		print(factorial)

		
1
2
6
24
120
720
5040
>>> 