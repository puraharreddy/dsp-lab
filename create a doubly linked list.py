# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 10:01:44 2020

@author: sony
"""
#purahar reddy , 22
#create a doubly linked list
class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.previous = None;    
        self.next = None;    
            
class DoublyLinkedList:    
    #Represent the head and tail of the doubly linked list    
    def __init__(self):    
        self.head = None;    
        self.tail = None;    
            
    #addNode() will add a node to the list    
    def addNode(self, data):    
        #Create a new node    
        newNode = Node(data);    
            
        #If list is empty    
        if(self.head == None):    
            self.head = self.tail = newNode;    
            self.head.previous = None;    
            self.tail.next = None;    
        else:    
            #newNode will be added after tail such that tail's next will point to newNode    
            self.tail.next = newNode;    
            newNode.previous = self.tail;    
            self.tail = newNode;    
            self.tail.next = None;    
                
    #display() will print out the nodes of the list    
    def display(self):    
        #Node current will point to head    
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        print("Nodes of doubly linked list: ");    
        while(current != None):     
            #Prints each node by incrementing pointer.    
            print(current.data),;    
            current = current.next;    
                
dList = DoublyLinkedList();    
#Add nodes to the list    
dList.addNode(22);    
dList.addNode(23);    
dList.addNode(24);    
dList.addNode(25);    
dList.addNode(26);    
     
#Displays the nodes present in the list    
dList.display();  

