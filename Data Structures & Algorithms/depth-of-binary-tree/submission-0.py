# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
DFS:
(if not root: return 0)
1. initialise a stack with root
2. initialise a int with value 1, and level = int
3. pop stack, find its neighbours
4. if neighbours +1 to int, append stack with neigbours
5.  
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        stack = [(root, 1)]
        dmax = 0
        
        while stack:
            current, depth = stack.pop()
            if current:
                dmax = max(dmax, depth)
            if current.left:
                stack.append((current.left, depth + 1))
            if current.right:
                stack.append((current.right, depth + 1))

        return dmax
