# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
DFS recursion:
1. if not root: return 0
2. return 1 + the max of child nodes
Thinking: at the end node it returns 1+ the max of 0 and 0 
and as we go up recursion stack we +1 with each level.
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
