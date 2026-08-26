class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxx = max(nums)
        counts = [0] * (maxx + 1)

        for n in nums:
            counts[n] += 1
        
        i = 0 
        for c in range(maxx + 1):
            while counts[c] > 0:
                nums[i] = c
                counts[c] -= 1
                i += 1
        

       
            
            
            
        

            
            
                



        