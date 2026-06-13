# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
"""
DFS:
1. Check if root is None or not then Take root 
2. find its neighbours 
3. flip them 
4. call recursively on the current node as root
5. Return root

"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:#1
            return None
        root.left, root.right = root.right, root.left#2,3
        self.invertTree(root.left)#4
        self.invertTree(root.right)#5
        return root

            



