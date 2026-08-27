from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        res = []

        for i in range(k):
            res.append(hashmap.most_common(k)[i][0])
        
        return res 