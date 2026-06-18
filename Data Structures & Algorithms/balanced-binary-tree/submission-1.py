# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
DFS to go to end node which returns an array of two values 
containing a value of height and boolean
value which gives if the tree is balanecd or not.
1. Base case: if not root: return [True, 0]
2. recursiveley call DFS with left and right node to reach end of recusrsive 
    stack.
3. balanced  =  left[0] and right[0] and abs(left[1] - right[1]) <= 1
4. return balanced and height(1 + max(left[1],right[1])) 
    and for answer only send back balanced
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1],right[1])]

        
        return dfs(root)[0]
        