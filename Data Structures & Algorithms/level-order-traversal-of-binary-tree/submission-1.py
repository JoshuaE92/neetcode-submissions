# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #implement a BFS

        #create a q, add the root to the q

        #
        #for all the elements inside the q
            #add of of the children inside the q/ret array
        
        #append that array
        if not root:
            return []
        q=deque([root])
        ret=[]

        while q:

            
            new=[]
            children=q.copy()
            
            for n in children:
                new.append(n.val)
            ret.append(new)
            
            for n in children:
                hi=q.popleft()
                if hi.left:
                   
                    q.append(hi.left)
                if hi.right:
                    
                    q.append(hi.right)
                
            
        return ret

            
            
                

        

        