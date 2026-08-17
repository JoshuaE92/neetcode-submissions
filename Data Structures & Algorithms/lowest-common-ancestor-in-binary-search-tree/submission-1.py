# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        #want to itreate through thre three looking for where the nodes are going to split, when u find the split u return the node that its att

        if(p.val<root.val and q.val<root.val):
            return self.lowestCommonAncestor(root.left, p,q)
        elif(p.val>root.val and q.val>root.val):
            return self.lowestCommonAncestor(root.right, p,q)
        else:
            return root

        