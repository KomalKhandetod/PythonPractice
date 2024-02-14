# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:59:14 2024

@author: S23233991
"""
x = []
y = []
d = []
    
def getlists():
    set=[]
    while True:
        s1=input("Please insert destination X2 value: ")
        s2=input("Please insert destination Y2 value: ")
        print("")
        if s1 == '999' or s2 == '999':
            return set
        n1=float(s1)
        n2=float(s2)
        x.append(n1)
        y.append(n2)

def distance(x,y):
    x1 = 0
    y1 = 0
    for i in range(len(x)):
        a = (x[i]-x1)**2
        #print ("a=",a)
        b = (y[i]-y1)**2
        #print("b=",b)
        dist = (a+b)**0.5
        #print("Dist=", dist)
        d.append(dist)
        #print(d)
        x1 = x[i]
        y1 = y[i]
        #print("X1=",x1)
        #print("Y1=",y1)
        i+=1
    return d
    
def total(set):
    totl=0.0
    for i in set:
        totl += i
    return totl

def result():   
    d=distance(x, y)
    for i in range(len(d)):
        j = i + 1
        print("Step %d: %.2f meter" %(j,d[i]))
        i+=1
    res = total(d)
    print("")
    print("Total distance (in meters) the robot has moved is : %.2f" %res)
    
set=getlists()
#print(x)
#print(y)
result()
