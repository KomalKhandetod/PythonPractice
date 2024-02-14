# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def anytimestable(x):
    for i in range(1,13):
        print("%d times %d is %d" %(i, x, i*x))
        
def getrangedint(min, max):
    while True:
        x = int(input("Enter a number between 1 and 12: "))
        if x >= min and x <= max:
            return x

table = getrangedint(1, 12)
anytimestable(table)

print("-------------------------------------------------")