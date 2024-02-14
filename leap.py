# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:31:39 2024

@author: S23233991
"""

def isleap(y):
    if y % 400 == 0:
        print("year %d is divisible by 400 but not by 100" %y)
        return True
    elif y % 100 == 0:
        print("year %d is divisible by 100" %y)
        return False
    elif y % 4 == 0:
        print("year %d is divisible by 4 but not by 100" %y)
        return True
    else:
        print("year %d is not divisible by any" %y)
        return False
#isleap(2013)

def daysinmonth(month,year):
    days = 0
    if month == 2:
       if (isleap(year) == True):
           days = 29
           return days
       else:
           days = 28
           return days
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        days = 30
        return days
    else :
        days = 31
        return days
    return days