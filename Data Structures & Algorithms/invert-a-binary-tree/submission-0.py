# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
"""
BFS:
1. make a queue with root initialised.
Loop this till the queue is empty:"
2. pop it out as current node and check its neighbor(l, r)
3. invert neighbours(left = right and opposite)
4. add neighbour to queue
"
5. return root
additionals:
if not root then return None
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])#1
        while queue:
            currentNode = queue.popleft()
            currentNode.left, currentNode.right = currentNode.right, currentNode.left#3
            if currentNode.left:#2
                queue.append(currentNode.left)#4
            if currentNode.right:
                queue.append(currentNode.right)#4
        return root

            



