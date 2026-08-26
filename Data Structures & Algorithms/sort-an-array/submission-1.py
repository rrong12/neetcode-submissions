class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1: 
            return nums
        
        a, b, c = nums[0], nums[len(nums) // 2], nums[-1]
        if (a <= b <= c) or (c <= b <= a): 
            p = b
        elif (b <= a <= c) or (c <= a <= b):
            p = a
        else:
            p = c


        L = [x for x in nums if x < p]
        R = [x for x in nums if x > p]
        P = [x for x in nums if x == p]


        L, R = self.sortArray(L), self.sortArray(R)
        
        return L + P + R
        
        