# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        
        for i in range(0, len(inorder)): 
            hashmap[inorder[i]] = i
            if inorder[i] == preorder[0]: 
                root_i = i
        self.pre_idx = 0 

        def dfs(l, r): 
            if l > r:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1 
            root = TreeNode(root_val)
            mid = hashmap[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root 

        return dfs(0, len(preorder) - 1)

            

