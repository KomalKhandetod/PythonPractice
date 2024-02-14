# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:52:02 2024

@author: S23233991
"""
def isprime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
            

def getrangedint(min):
    while True:
        x = int(input("Enter a number greater than 2: "))
        if x > min:
            return x
        
total = getrangedint(2)

for num in range(2, total):
    if isprime(num):
        print(num)
        
print("-------------------------------------------------")
