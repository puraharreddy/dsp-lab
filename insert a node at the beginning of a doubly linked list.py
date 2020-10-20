# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:03:35 2020

@author: sony
"""
#purahar reddy , 22
#insert a node at the beginning of a doubly linked list
  
class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.previous = None;    
        self.next = None;    
            
class InsertStart:    
    #Represent the head and tail of the doubly linked list    
    def __init__(self):    
        self.head = None;    
        self.tail = None;    
            
    #addAtStart() will add a node to the starting of the list    
    def addAtStart(self, data):    
        #Create a new node    
        newNode = Node(data);    
            
        #If list is empty    
        if(self.head == None):     
            self.head = self.tail = newNode
            self.head.previous = None;
            self.tail.next = None;    
        #Add newNode as new head of the list    
        else:    
            self.head.previous = newNode;    
            newNode.next = self.head;    
            newNode.previous = None;    
            self.head = newNode;    
                
    #display() will print out the nodes of the list    
    def display(self):    
        #Node current will point to head    
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        print("Adding a node to the start of the list: ");    
        while(current != None):    
            #Prints each node by incrementing pointer.    
            print(current.data),    
            current = current.next;    
                
        print();    
            
dList = InsertStart();    
     
#Adding 1 to the list    
dList.addAtStart(22);    
dList.display();    
#Adding 2 to the list    
dList.addAtStart(23);    
dList.display();    
#Adding 3 to the list    
dList.addAtStart(24);    
dList.display();    
#Adding 4 to the list    
dList.addAtStart(25);    
dList.display();    
#Adding 5 to the list    
dList.addAtStart(26);    
dList.display();    

