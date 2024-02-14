# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:12:01 2024

@author: S23233991
"""
import math
'''
def print_name(first, last):
    print("First name %s " %first)
    print("Last name %s " %last)
fn = "Albert"
ln= "Einstein"
print_name(fn, ln)
print_name(last="Einstein", first="Albert")
print_name(fn, last="Einstein")
print_name(ln, first="Albert")
print("------------------------------")
'''
def change_val(num):
    num += 100
    print("Inside parameter value %d" %num)
val = 100
print("Argument value %d" %val)
change_val(val)
print("Argument value after function call %d" %val)

print("------------------------------")

'''
def get_name():
    first = input("Enter first name : ")
    last = input("Enter last name : ")
    return first, last
f_name, l_name = get_name()
print(f_name)
print(l_name)
'''
print("------------------------------")

def add_numbers(n1, n2):
    summation = n1 + n2
    print("Here is sum %d" %summation)
add_numbers(10, 5)
print("------------------------------")
print(abs(-12))
print(abs(min(max(-12, 5), -15)))
print(min(sum(range(1, 10, 2)),sum(range(2, 10, 2))))
print(max(round(25.64,0), round(25.64,2)))
print(len("This is a test"))
print("---------------------")
print(math.sqrt(7))
print(max(math.copysign(25, -2.0),sum([-5,-7,-15])))
print(min(math.ceil(-4.5), math.floor(-5.2)))
print(max(math.trunc(-6.6), math.floor(-6.6)))
print("----------------------------")