# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path1 = path2 = []
        path = []
    
        def search(node, target):
            if node.val == target.val: return [node] 
            if node.val < target.val: return [node] + search(node.right, target)
            return [node] + search(node.left, target)
        
        path1 = search(root, p)
        path2 = search(root, q)

        i = 0 
        while True: 
            if i == len(path1): 
                return path1[i-1]
            if i == len(path2):
                return path2[i-1]
            if path1[i] == path2[i]:
                i += 1
            else:
                break
        
        return path1[i-1]
            


             
