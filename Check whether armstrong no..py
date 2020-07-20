Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input('Enter a number: '))
Enter a number: 153
>>> sum=0
>>> temp=num
>>> while temp > 0:
	digit= temp%10
	sum += digit**3
	temp //=10

	
>>> if num==sum:
	print(num,'is an armstrong number')
else:
	print(num,'is not an armstrong number')

	
153 is an armstrong number
>>> 