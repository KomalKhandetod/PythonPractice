# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:54:47 2024

@author: S23233991
"""

def add(a,b):
    s = a+b
    return s

def sub(a,b):
    s = a-b
    return s

def mul(a,b):
    s = a*b
    return s

def div(a,b):
    s = a/b
    return s

def calculate(a,b,operation):
    if(operation=="+"):
        s = add(a, b)
        print("Adding %d and %d = %d" %(a,b,s))
    elif(operation=="-"):
        s = sub(a, b)
        print("Subtracting %d from %d = %d" %(b,a,s))
    elif(operation=="*"):
        s = mul(a, b)
        print("Multiplying %d by %d = %d" %(a,b,s))
    elif(operation=="/"):
        s = div(a, b)
        print("Dividing %d by %d = %f" %(a,b,s))
    else:
        s=''
    return s

def main():
    print("Welcome to Python Calculator")
    a = int(input("Input Number 1: "))
    b = int(input("Input Number 2: "))
    operation = input("Select an operator * for multiplication, - for subtraction, + for addition, / for division: ")
    result = calculate(a,b,operation)
    if(result==''):
        print("Invalid operation entered!!")
    else:
        print("Results: ", result)

main()