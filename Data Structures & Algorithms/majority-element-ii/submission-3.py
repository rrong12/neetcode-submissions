class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        val = (len(nums) / 3) - 1
        res = []
        count = 0 
        print(nums)
        if len(nums) == 1:
            return nums
        if len(nums) == 2: 
            return nums
       
        for i in range(1, len(nums)):
            
            if nums[i] == nums[i-1]:
                count += 1
            else: 
                count = 0 
            
            if count > val:
                if len(res) <= 0: 
                    res.append(nums[i])
                elif res[-1] != nums[i]:
                    res.append(nums[i])
        
        return res

