# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:50:12 2024

@author: S23233991
"""

name = input("Enter your name")
weight = float(input("Enter your Weight"))
height = float(input("Enter your Height"))

def bmi_cal(weight,height):
    BMI = weight/(height*height)
    if BMI<=18.5:
        print("%s you are Underweight" %name)
    elif (BMI >= 18.5 and BMI <=24.9):
        print("%s you are Healthy" %name)
    elif (BMI>=25.0 and BMI<=29.9):
        print("%s you are Overweight" %name)
    else:
        print("%s you are obese" %name)
    return BMI

print("Your BMI is ", bmi_cal(weight, height))


    
