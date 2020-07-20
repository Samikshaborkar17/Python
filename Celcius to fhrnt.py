Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #in order to convert celcius into fahrenheit celcius has to be initially multiplied by 1.8 and then 32 is to be added
>>> 
>>> c = float(input('Enter the temperaturte in celcius: '))
Enter the temperaturte in celcius: 37
>>> confactor1 = 1.8
>>> midstep = c* confactor1
>>> f = midstep + 32
>>> print('The given temperature in celcius is following fhrnt: ',f)
The given temperature in celcius is following fhrnt:  98.60000000000001
>>> 