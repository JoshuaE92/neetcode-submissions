"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #crate a hashmap to store old vars

        #make a function to take in the root node

        #base case

        #if not create the node 

        #loop through the current node children
        #append the cur nodes children to the copy

        #return node

        oldtonew={}

        def clone(node):

            if node in oldtonew:
                return oldtonew[node]
            else:
                copy=Node(node.val)
                oldtonew[node]=copy
                for nei in node.neighbors:
                    copy.neighbors.append(clone(nei))
                return copy
           
            

        if node:
            return clone(node)
        else:
            return None



        



        




        