# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case of emtpy return 0

        #a value or just 1
        #go left, 1+function call
        # go right return 1 plus function call
        #return max between both sides


        if root ==None:
            return 0

        left=1+self.maxDepth(root.left)
        right=1+self.maxDepth(root.right)

        return max(left,right)


        #BFS

        #define our q
        #iterate through the 
        #while we still have elements in the q
        #pop the current value
        #add the current values left to the q
        #add teh current values right to the q
        #add to the levels
        #return levles

        q=deque[root]
        levels=0

        while q:

            for i in range(len(q)):
                node=q.popleft()
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            levels+=1
            
        return levels
            
                


        