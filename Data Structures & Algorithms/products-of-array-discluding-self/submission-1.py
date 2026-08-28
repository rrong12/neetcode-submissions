class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref = [1]
        sufi = [1]

        n = len(nums)
        for i in range(n): 
            pref.append(pref[-1] * nums[i])
            sufi.append(sufi[-1] * nums[-1 - i])
        
        res = []
      
        p = 0
        s = 0
 
        ps_len = len(pref)

        for i in range(n): 
            if i == 0: 
                res.append(sufi[-2])
            elif i == n - 1:
                res.append(pref[n - 1])
            else:
                res.append(sufi[n - 1 - i] * pref[i])

            
        
        return res

        