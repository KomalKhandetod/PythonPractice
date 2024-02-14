# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:26:26 2024

@author: S23233991
"""

#a. Try using %s to interpolate a string inside a string.

str1 = input("Enter a string")
print("You entered: %s" %str1)

''' b. Experiment with getting %d, %f and %s int, float and string interpolations the wrong
way around compared to the literal or variable values, e.g., see what happens when you
evaluate:
"Incorrect type %.2d" % 5.5'''

print("Incorrect type %.2d" % 5.5)

#c. Try a selection of mismatched conversions and observe the results.
age = 32
name = 'Rock'
print("Name is %s and Age is %d" %(name,age))

'''d. Experiment with putting a number between % and d, f or s when interpolating a value
into a string e.g., %10s . Then try putting a dot before the number e.g. %.10s . Then try
putting numbers both sides of the dot. e.g. %10.2f . '''

_float1 = 35.986537
print("Float number is %5.4f" %_float1)

str2 = "logic is good"
print("Interpolation %50s"%str2)