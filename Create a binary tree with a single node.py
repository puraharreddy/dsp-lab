# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:00:16 2020

@author: sony
"""
#purahar reddy, 22
#Creating a binary tree with a single node
#class
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    #print
    def PrintTree(self):
        print(self.data)
tree=Node(15)
#calling print function
tree.PrintTree()

