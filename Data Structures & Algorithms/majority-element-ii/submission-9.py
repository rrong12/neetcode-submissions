class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            elif len(counts) < 2:
                counts[n] = 1
            else:
                for key in list(counts):
                    counts[key] -= 1
                    if counts[key] == 0:
                        del counts[key]

        threshold = len(nums) // 3
        return [c for c in counts if nums.count(c) > threshold]