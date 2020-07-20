Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> terms = int(input('Enter the number of terms: '))
Enter the number of terms: 10
>>> n1=0
>>> n2=1
>>> count=0
>>> if terms<=0:
	print('Please enter a non negative term')
elif terms==1:
	print(n1)
else:
	while(count<terms):
		print(n1)
		nth=n1+n2
		n1=n2
		n2=nth
		count += 1

		
0
1
1
2
3
5
8
13
21
34
>>> 