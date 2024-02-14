# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:32:29 2024

@author: S23233991
"""

def getrangedint():
    print("Testing for loop exit at the top")
    min, max = 1, 12
    x=0
    while x < min or x > max:
        x = int(input("enter a number between 1 and 12: "))
    return x

getrangedint()

print("--------------------------------------------------------")
def getrangedint_1():
    print("Exiting at the loop bottom")
    min, max = 1, 12
    while True:
        x = int(input("enter a number between 1 and 12: "))
        if x >= min and x <= max:
            return x
        
getrangedint_1()

print("--------------------------------------------------------")

def getrangedint_2(min, max):
    print("Exiting at the loop bottom")
    while True:
        x = int(input("enter a number between 1 and 12: "))
        if x >= min and x <= max:
            return x

getrangedint_2(1,12)

print("--------------------------------------------------------")

print("Exiting in the middle of a loop")
def getlist():
    set=[]
    while True:
        s=input("Enter a number or * to quit: ")
        if s == '*':
            return set
        n=float(s)
        set.append(n)

def total(set):
    totl=0.0
    for i in set:
        totl += i
        return totl

set=getlist()
print(total(set))

print("--------------------------------------------------------")

def isprime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
        return True

def listcompounds_ge(y):
    while not isprime(y):
        print(y)
        y += 1

listcompounds_ge(13)
listcompounds_ge(98)
listcompounds_ge(999)

print("--------------------------------------------------------")