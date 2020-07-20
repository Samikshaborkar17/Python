Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lower = 100
>>> upper = 4000
>>> for num in range(lower,upper+1):
	order=len(str(num))
	sum=0
	temp=num
	while(temp>0):
		digit=temp%10
		sum += digit**order
		temp //= 10
	if(num==sum):
		print(num)

		
153
370
371
407
1634
>>> 
>>> 
>>> lower = 100
>>> upper =4000
>>> for num in range(lower,upper+1):
	sum=0
	temp=num
	order=len(str(num))
	while(temp>0):
		digit=temp%10
		sum += digit**order
		temp //= 10
	if(num==sum):
		print(num)

		
153
370
371
407
1634
>>> 
>>> 
>>> lower = 100
>>> upper = 4000
>>> for num in range(lower,upper+1):
	sum=0
	temp=num
	order=len(str(num))
	while(temp>0):
		digit=temp%10
		sum += digit**order
		temp //= 10
		if(num==sum):
			print(num)

			
125
153
216
370
371
407
729
1296
1634
>>> #wrong output hence proper looping is very important