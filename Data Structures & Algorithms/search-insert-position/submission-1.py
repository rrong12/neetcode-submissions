class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r: 
            m = (l + r) // 2
            if nums[m] == target: 
                return m
            if nums[m] > target: 
                r = m - 1
            else: 
                l = m + 1

        if target < nums[0]: 
            return 0 

        if target > nums[-1]: 
            return len(nums)
        if l == r: 
            if target < nums[l]: 
                return l - 1
            else: 
                return l + 1
        
        elif l > r: 
            if nums[r] < target: 
                return r + 1
            else: 
                return r - 1



    '''
 [-1,0,2,4,6,8]
 l = 0, r = 5
 l = 3, r = 5, m = 4 
 l = 3, r = 3, m = 3, not found 
    '''