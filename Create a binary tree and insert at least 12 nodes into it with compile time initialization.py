# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:01:33 2020

@author: sony
"""
#purahar reddy, 22
#Creating a binary tree and inserting at least 12 nodes into it with compile time initialization
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
#insert method to add nodes
tree=Node(4)
tree.insert(3)
tree.insert(12)
tree.insert(8)
tree.insert(54)
tree.insert(57)
tree.insert(64)
tree.insert(91)
tree.insert(108)
tree.insert(30)
tree.insert(3)
tree.insert(12)
tree.PrintTree()

