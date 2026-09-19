# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
edge cases: 

'''
class Solution:
    def dfs(self, node):
            if node is None:
                return 0
            return 1 + max(self.dfs(node.left), self.dfs(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None: 
            return True
        
        if abs(self.dfs(root.left) - self.dfs(root.right)) > 1:
            return False 
        
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        
        return True
      