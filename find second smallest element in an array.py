# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 09:53:09 2020

@author: sony
"""
#purahar reddy, 22
#program to find second smallest element in an array
#input array
arr=[]
n=int(input("enter range: "))
print("enter array elements: ")
for i in range(n):
    ele=int(input())
    arr.append(ele)
arr.sort()
print(arr[1])

