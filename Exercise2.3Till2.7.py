# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:34:59 2024

@author: S23233991
"""

print(type([]))
print(type([2,4]))
print(type(['hello', 10.5]))

l=[2,3]
l.append(5)
print(l)
l.insert(0,1)
print(l)
l.insert(2,4)
print(l)
print(l[1])
print(l[4])

print(len(l))
print(len("this"))
print(len((0,)))


l.reverse()
print(l)
l.sort()
print(l)
del l[1]
print(l)
del l[3]
print(l)

print(list(range(1,10)))
print(list(range(1,20,2)))
print(list(range(3,20,3)))
print(list( range(20,0,-1)))
a=list(range(1,11))
print(a)
print(a[3:5])
print(a[:])
print(a[:6])
print(a[6:])

b=a
c=a[:]
a.remove(3)
print(a)
print(b)
print(c)
