# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
DFS recursive:
1. Define a global variable res = 0 which is our expected max-diameter
2. We define a function which calculates the height for each node on 
left and right by which we can calculate the max diameter so far as:
    res = max(res, left + right)
3. Inside DFS: The function is recursively returning the maximum height
on either side while updating res. So: return max(left,right) + 1. We add
1 since the node above has 1 extra height.
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left + right)

            return 1 + max(left,right)

        dfs(root)
        return res
