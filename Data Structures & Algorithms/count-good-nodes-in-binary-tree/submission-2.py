# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        dfs, store the max each time going down, if the node is greater than the max, increase count by 1 
        """
        res = 0
        
        def dfs(node, local_max):
            nonlocal res
            if not node: 
                return None 
            
            if node.val >= local_max:
                res += 1
                local_max = max(node.val, local_max)
            
            dfs(node.left, local_max)
            dfs(node.right, local_max)
        
        dfs(root, -101)
        return res
        
        