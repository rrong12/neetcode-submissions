class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l, r = 0, 1

        while r < len(prices): 

            if prices[r] > prices[l]:
                prof = max(prices[r] - prices[l], prof)
        
            else:
                l = r
            
            r += 1
        
        return prof