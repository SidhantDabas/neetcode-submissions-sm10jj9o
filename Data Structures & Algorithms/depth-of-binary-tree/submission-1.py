# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
DFS:
(if not root: return 0)
1. initialise a stack with root and the depth = 1
2. initialise a int with value 0 used for maximum depth
Create a loop until stack empties
3. pop stack, find whats bigger? the maximum depth or current level depth
4. if neighbour, append stack with the neighbour and their depth(current level depth + 1)

5. Return max depth 
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        stack = [(root, 1)]#1
        dmax = 0#2
        
        while stack:
            current, depth = stack.pop()
            if current:
                dmax = max(dmax, depth)#3
                stack.append((current.left, depth + 1))
                stack.append((current.right, depth + 1))

        return dmax
