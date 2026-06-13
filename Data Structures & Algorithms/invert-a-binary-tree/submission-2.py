# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
"""
DFS iteratively:
1. Check if root is None or not
2. initialise a stack with root
3. check its neighbours
4. flip its neighbours
5. put neighbours on stack
6. Loop until stack is empty
7. Return root

"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:#1
            return None
        stack = [root]#2
        while stack:#6
            current = stack.pop()
            current.left, current.right = current.right, current.left#3,4
            if current.left:#5
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

            
        return root#7

            



