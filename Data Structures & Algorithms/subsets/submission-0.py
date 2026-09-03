class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def search(i):
            if i == n: 
                res.append(sol[:])
                return
            
            search(i + 1)
            sol.append(nums[i])
            search(i + 1)
            sol.pop()
        
        search(0)
        return res

            
