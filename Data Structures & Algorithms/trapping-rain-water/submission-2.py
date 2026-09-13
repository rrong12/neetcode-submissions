class Solution:
    def trap(self, height: List[int]) -> int:
        prefmax, sufmax = [0] * len(height), [0] * len(height)
        temp = 0 

        for i in range(len(height)):
            temp = max(temp, height[i])
            prefmax[i] = temp
        
        temp = 0 

        for j in range(len(height) - 1, -1, -1):
            temp = max(temp, height[j])
            sufmax[j] = temp
        
        i, res = 0, 0
        for i in range(len(height)):
            res += min(prefmax[i], sufmax[i]) - height[i]
        
        return res


