class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)

        while l < r:
            m = (l + r) // 2
            
            if nums[m] < nums[m-1]: 
                return nums[m]

            if nums[m] > nums[-1]:
                l = m + 1

            else:  
                r = m - 1

        if l == len(nums): return nums[0]
        else: return nums[l]
            

