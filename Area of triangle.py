Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Initially find semiperemeter and then the area
>>> #Semiperemeter - (a+b+c)/2
>>> #Area - Sq Root Of (s*(s-a)*(s-b)*(s-c))
>>> 
>>> a= float(input("Side1 of the triangle measures: "))
Side1 of the triangle measures: 5
>>> b= float(input("Side2 of the triangle measures: "))
Side2 of the triangle measures: 6
>>> c= float(input("Side3 of the triangle measures: "))
Side3 of the triangle measures: 7
>>> s= (a+b+c)/2
>>> print('semiperemeter of the triangle measures: ',s)
semiperemeter of the triangle measures:  9.0
>>> area= (s*(s-a)*(s-b)*(s-c))**0.5
>>> print('The area of the triangle is: ',area)
The area of the triangle is:  14.696938456699069
>>> 