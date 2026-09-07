class Solution:
    def mySqrt(self, x: int) -> int:

        # i * i <= x

        l = 1
        r = x
        res = 0 

        while l <= r: 
            m = (l + r) // 2
           
            if m * m <= x:
                res = max(res, m)
                l = m + 1
            else:
                r = m - 1
        
        return res