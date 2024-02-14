# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:19:16 2024

@author: S23233991
"""
import math

x = ('abc',20.69,30)
print("Values to be tested are: ")
print(x)
#print(type(x))

a = x[0]
#print(a)
#print(type(a))
b = x[1]
#print(b)
#print(type(b))
c = x[2]
#print(c)
#print(type(c))
 
def typeCompare(y):    
    if(type(math.pi) == type(y)):
        val2 = y**2
        print(val2)
    elif(type(10) == type(y)):
        val2 = y**2
        print(float(val2))
    else:
        print("Sorry Dave, I'm afraid I can't do that")
        val2 = 0.0
        print(val2)
    return val2
    
typeCompare(a)
typeCompare(b)
typeCompare(c)