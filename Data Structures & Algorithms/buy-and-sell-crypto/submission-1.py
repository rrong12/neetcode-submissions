class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l = 0
        r = 0 

        while r < len(prices): 
            while r < len(prices) and prices[r] < prices[l]: 
                l += 1
                r = l + 1
            
            if r < len(prices): 
                prof = max(prices[r] - prices[l], prof)
            r += 1
                
                #print(pricaes[l])
                #print(prices[r])
                #print(prof)


        return prof