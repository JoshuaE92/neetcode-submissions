# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #normal dfs transversal
        #at each step ask, are both current nodes the same
        #if so go down right and left
        #if they are not the same, return false
        #retufn true if u never returned false

        ##def issame(p,q):
            ##retval1=False
            ##retval2=False
           ## if p==None and q==None:
                ##return True
           ## elif p and q:
                
                    ##if(p.val==q.val):
                        ##retval1=self.isSameTree(p.left,q.left)
                        ##retval2=self.isSameTree(p.right,q.right)
                    ##else:
                        ##return False
           
            
            
            ##return retval1==True and retval2==True

        ##return issame(p,q)

        if not p and not q:
            return True
        if not p or not q or (p.val!=q.val):
            return False
        
        return(self.isSameTree(p.left,q.left)==True and self.isSameTree(p.right,q.right)==True)







            

        
        