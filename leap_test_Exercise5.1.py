# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:39:54 2024

@author: S23233991
"""

import sys
sys.path.append("Z:\CMP7244\Lab2")
import leap

print(sys.path)
print(leap.isleap(1900))
print(leap.isleap(2000))
print(leap.isleap(2012))
print(leap.isleap(2019))
print("")
print("Exercise 5.1: Days in a month")
monthNumber = int(input("Enter the number of the month between 1 and 12"))
yearNumber = int(input("Enter the number of the year YYYY"))

dayCount = leap.daysinmonth(monthNumber, yearNumber)

if (dayCount == 28):
    print("This month is February and has 28 days!")
elif (dayCount == 29):
    print("This month is February and has 29 days, as it is a leap year!")
elif (dayCount == 30):
    print("The months September, April, June and November have 30 days!")
else:
    print("This month has 31 days!")

