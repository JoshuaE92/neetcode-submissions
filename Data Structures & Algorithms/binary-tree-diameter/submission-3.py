# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        #base case is if the the val is null:
            #return 0
        
        #dfs

        #return 1+max(left,right)
        
        def dfs(root):
            
            if root==None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            
            self.res=max(self.res,left+right)
            
            
            return 1+max(dfs(root.left),dfs(root.right))
        
        dfs(root)
        return self.res