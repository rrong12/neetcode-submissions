from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        res = []

        top = hashmap.most_common(k)
        for i in range(k):
            res.append(top[i][0])
        
        return res 