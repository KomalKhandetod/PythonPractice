# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:05:19 2024

@author: S23233991
"""
def percentage(x):
    perct = (x/35)*100
    per = round(perct)
    return per


print("Housing Occupancy Census Report")
occupants0 = int(input("Provide the number of houses with 0 Occupancy: "))
per0 = str(percentage(occupants0))+"%"
occupants1 = int(input("Provide the number of houses with 1 Occupancy: "))
per1 = str(percentage(occupants1))+"%"
occupants2 = int(input("Provide the number of houses with 2 Occupancy: "))
per2 = str(percentage(occupants2))+"%"
occupants3 = int(input("Provide the number of houses with 3 Occupancy: "))
per3 = str(percentage(occupants3))+"%"
occupants4 = int(input("Provide the number of houses with 4 Occupancy: "))
per4 = str(percentage(occupants4))+"%"
occupants5 = int(input("Provide the number of houses with 5 Occupancy: "))
per5 = str(percentage(occupants5))+"%"
occupants6 = int(input("Provide the number of houses with 6 Occupancy: "))
per6 = str(percentage(occupants6))+"%"
occupants7 = int(input("Provide the number of houses with 7 Occupancy: "))
per7 = str(percentage(occupants7))+"%"
print("Occupants     0     1     2     3     4     5     6     >6")
print("No. houses    %d    %d    %d    %d    %d    %d    %d    %d" %(occupants0,occupants1,occupants2,occupants3,occupants4,occupants5,occupants6,occupants7))
print("Percentage    %s    %s    %s    %s    %s    %s    %s    %s" %(per0,per1,per2,per3,per4,per5,per6,per7)) 
