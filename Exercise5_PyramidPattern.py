# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:39:20 2024

@author: S23233991
"""

def half_pyramid(rows):
    for r in range(1, rows + 1):
        for c in range(1, r + 1):
            print("*", end=" ")
        print()

def pyramid(rows):
    k = rows - 1
    for i in range(0, rows):
        for j in range(0, k):
            print(end=" ")
        k -= 1
        for j in range(0,i+1):
            print("*", end=" ")
        print()
    
half_pyramid(5)
pyramid(5)