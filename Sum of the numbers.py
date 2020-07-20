Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = 7
>>> num2 = 5
>>> sum = num1+ num2
>>> print(sum)
12
>>> Num1 = int(input("Enter the first number: "))
Enter the first number: 7
>>> Num2 = int(input("Enter the second number: "))
Enter the second number: 5
>>> sum = Num1 + Num2
>>> print("Sum of the number {0} and {1} is {2}" .format(Num1, Num2, Sum))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print("Sum of the number {0} and {1} is {2}" .format(Num1, Num2, Sum))
NameError: name 'Sum' is not defined
>>> print(Sum, "The sum of the numbers is: ")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(Sum, "The sum of the numbers is: ")
NameError: name 'Sum' is not defined
>>> print("Sum of the numbers is: ")
Sum of the numbers is: 
>>> print(sum)
12
>>> print( sum,'sum of the numbers is: ')
12 sum of the numbers is: 
>>> print('sum of the numbers is: ',sum)
sum of the numbers is:  12
>>> 