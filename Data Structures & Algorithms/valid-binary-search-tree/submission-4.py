# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversal, stack = [], []
        node = root

        while node or stack: 
            while node: 
                stack.append(node)
                node = node.left
            node = stack.pop()
            traversal.append(node.val)
            node = node.right 
        
        for i in range(1, len(traversal)):
            if traversal[i - 1] >= traversal[i]:
                return False
        
        return True