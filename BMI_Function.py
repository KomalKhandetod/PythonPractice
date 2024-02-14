# -*- coding: utf-8 -*-

"""
Created on Mon Jan 29 10:13:30 2024

@author: S23233991
"""
name = input("Enter your name")
weight1 = float(input("Enter your Weight"))
height1 = float(input("Enter your Height"))

def bmi_cal(weight,height):
    BMI = weight/(height*height)
    return BMI

print("%s your BMI is" %name, bmi_cal(weight1, height1))




