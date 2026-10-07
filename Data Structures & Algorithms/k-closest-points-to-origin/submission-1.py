import math 
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #store heap info as (dist, [x, y])
        #juh keep popping it to get the k closest
        res = []
        heap = []
        #loop through all, 0(n) 
        for x, y in points: 
            dist = math.sqrt(x ** 2 + y ** 2)
            heap.append((dist, [x, y]))
            heapq.heapify(heap)
        
        for i in range(k): 
            res.append(heapq.heappop(heap)[1])
        
        return res