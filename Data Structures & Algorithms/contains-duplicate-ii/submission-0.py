from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = defaultdict(list)

        for i, n in enumerate(nums):
            hashmap[n].append(i)
        
        for key in hashmap:
            for ind in range(1, len(hashmap[key])):
                if abs(hashmap[key][ind] - hashmap[key][ind - 1]) <= k:
                    return True
        
        return False


        