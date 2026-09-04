class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # sort the array
        # [4, 10, 23, 25], h = 4
        # min k is 4, max k is 25, mid k is 14
        # [25, 23, 10, 4], h = 6, k = 15 
        # calc hours by simulating through the array
        # while piles[-1] != 0
        # perform binary search, while min_k <= max_k
        # o(nlogn), space is o(1)
       

       piles.sort()
       min_k, max_k = piles[0] // h, piles[-1]


       while min_k < max_k: 
            mid_k = (min_k + max_k) // 2
            if mid_k == 0:
                return 1
            
            hours = 0 

            for b in piles: 
                hours += (b + mid_k - 1) // mid_k
            
            if hours > h:
                min_k = mid_k + 1

            else:
                max_k = mid_k
               

       return min_k



        