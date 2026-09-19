# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        prev_c = 1
        
        if root is None:
            return []
            
        while q: 
            curr_res = []
            curr_c = 0 
            for i in range(0, prev_c):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    curr_c += 1
                if node.right:
                    q.append(node.right)
                    curr_c += 1
                curr_res.append(node.val)
            res.append(curr_res)
            prev_c = curr_c
        
        return res

