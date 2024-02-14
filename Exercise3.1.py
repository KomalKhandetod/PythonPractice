# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:49:07 2024

@author: S23233991
"""

import sys
sys.path.append('Z:\CMP7244\Lab4')
import times_table

a = int(input("Enter any value between 1 to 12: "))
times_table.timestable(a)

print("-----------------------------------------------------")

for i in range(1, 13):
    times_table.timestable_1(i)
    print()
    
