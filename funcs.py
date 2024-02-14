# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:44:19 2024

@author: S23233991
"""
import math

#radius1 = float(input("Enter the radius of the circle: "))
def areacirc(radius):
    Pi = math.pi
    area = radius * Pi
    print("Radius is %0.2f and area is %0.2f" %(radius,area))
    return area

#areacirc(radius1)

def rectarea(w,h):
    rarea = w*h
    print("Width is %0.2f and Height is %0.2f" %(w,h))
    print("Area of rectangle is %0.2f" %rarea)
    return rarea
'''
Width = float(input("Input Width of the rectangle:"))
Height = float(input("Input Height of the rectangle:"))

rectarea(Width, Height)'''

