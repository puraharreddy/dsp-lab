# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:18:12 2020

@author: sony
"""
# Linked list node  
class Node: 
  
    def __init__(self): 
        self.data = None
        self.next = None
  
head = None
  
# Function that returns the largest element    
def largestElement(head):  
  
    max = -32767
  
    while (head != None): 

        if (max < head.data) : 
            max = head.data  
        head = head.next
      
    return max
  
# Function that returns smallest element 
def smallestElement(head):  
   
    min = 32767

    while (head != None) :
        
        if (min > head.data) : 
            min = head.data  
        head = head.next
      
    return min
  
# Function that push the element in linked list.  
def push( data) : 
  
    global head 
  
    # Allocate dynamic memory for newNode.  
    newNode = Node()  
  
    # Assign the data into newNode.  
    newNode.data = data  
  
    # newNode.next assign the address of  
    # head node.  
    newNode.next = (head)  
  
    # newNode become the headNode.  
    (head) = newNode  
  
# Display linked list.  
def printList( head) : 
  
    while (head != None) : 
        print(head.data ,end= " -> ")  
        head = head.next
      
    print("None")  
  
# execution starts here
push(60)  
push(300)  
push(20)  
push(15)  
push(30)
push(100)
push(50)
print("Linked list is : ")  
  
# display the linked list.  
printList(head)  
print("Maximum element in linked list: ",end="")  
   
# largest element in linked list.  
print(largestElement(head))  
print("Minimum element in linked list: ",end="")  
  
# smallest element in linked list.  
print(smallestElement(head),end="")


