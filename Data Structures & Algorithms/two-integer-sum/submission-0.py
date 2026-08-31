class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        i = 0
        j = len(nums) - 1
        pair = []

        for i, num in enumerate(nums):
            pair.append([num,i])

        pair.sort()

        i = 0 
        while i < j: 
            res = pair[i][0] + pair[j][0]

            if res == target:
                return [min(pair[i][1], pair[j][1]),
                        max(pair[i][1], pair[j][1])]
            if res > target:
                j -= 1
            if res < target:
                i += 1
        
        return []
