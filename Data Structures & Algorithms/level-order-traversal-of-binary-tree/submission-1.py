# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        que = deque([root])
        while que:
            level = []
            # The current size of the queue is exactly how many nodes are on this level
            level_size = len(que) 
            
            for i in range(level_size):
                cur = que.popleft()
                level.append(cur.val)
                
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            
            # Append a fresh copy of the level data
            res.append(level) 
            
        return res
            
"""
BFS makes a queue and puts in the new nodes while releasing th old ones
What if i make a counter of elements for a level.
For output need a list of list.
"""
