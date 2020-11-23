# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:19:50 2020

@author: sony
"""
#purahar reddy, 22
#to implement selection sort using recursive
def minIndex( a , i , j ): 
    if i == j: 
        return i 
          
    # Find minimum of remaining elements 
    k = minIndex(a, i + 1, j) 
      
    # Return minimum of current and remaining. 
    return (i if a[i] < a[k] else k) 
      
# Recursive selection sort. n is  size of a[] and index is index of  starting element. 
def recurSelectionSort(a, n, index = 0): 
  
    # Return when starting and  size are same 
    if index == n: 
        return -1
          
    # calling minimum index function  for minimum index 
    k = minIndex(a, index, n-1) 
      
    # Swapping when index and minimum index are not same 
    if k != index: 
        a[k], a[index] = a[index], a[k]
        recurSelectionSort(a, n, index + 1) 
      
# Driver code 
arr = []
m = int(input("Enter range:"))
for i in range(m):
    ele = int(input())
    arr.append(ele)
n = len(arr) 
  
# Calling function 
recurSelectionSort(arr, n) 
  
# printing sorted array 
for i in arr: 
    print(i,end = ' ')
