# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        #want to itreate through thre three looking for where the nodes are going to split, when u find the split u return the node that its att

        cur=root
        while cur:

            if(p.val<cur.val and q.val<cur.val):
                 cur=cur.left
            elif(p.val>cur.val and q.val>cur.val):
                 cur=cur.right
            else:
                return cur

        