class Solution:
    def maxArea(self, heights: List[int]) -> int:

        f, l = 0, len(heights) - 1
        max_area = 0

        while f < l: 
            area = (l - f) * min(heights[f], heights[l])
            if area > max_area:
                max_area = area

            if heights[f] > heights[l]:
                l -= 1
            else:
                f += 1
        
        return max_area

  