# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 

        def dfs(curr):
            nonlocal res 
            if curr is None: return 0

            res = max(res, dfs(curr.left) + dfs(curr.right))

            return 1 + max(dfs(curr.left), dfs(curr.right))

        dfs(root)
        return res