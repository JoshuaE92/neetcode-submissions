# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
       # if we have root and not the subroot:ret true 
       #if we dont ahve the root and have the subroot: return false
       #is the tree the same? return fture
       #if not, go the the left subtree  and go to the rightsubtree and return if either or is correct


       #helper function
       #do we not have nay nodes: return true
       #if we have both node and they are not the same:refalse
       #if they are the same return if the left is true and the right is true


        def isSame(root,subroot):
            if not root and not subroot:
                return True
            if root and subroot and root.val==subroot.val:
            
                return (isSame(root.left,subroot.left) and isSame(root.right,subroot.right))
            return False
               


        if  not subRoot:
            return True
        if not root and subRoot:
            return False
        
        if isSame(root,subRoot):
            return True

        
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

        





         
       
        




       
        

        