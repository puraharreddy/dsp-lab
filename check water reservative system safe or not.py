# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 09:17:50 2020

@author: sony
"""
#purahar reddy , 22
st=input("Enter string: ")
s=[]
f=0
count=0
o="("
c=")"
def checkclose(k):
    if c.index(k)!=o.index(s[-1]):
        return False
    return True
for i in st:
    if i in o:
        s.append(i)
    else:
        if len(s)==0:
            f=1
            break
        if checkclose(i):
            count+=1
            s.pop()
if f==1 or len(s)!=0:
    print("Not safe")
else:
    print(count)
