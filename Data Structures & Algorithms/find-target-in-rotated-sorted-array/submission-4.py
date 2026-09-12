class Solution:

    def search(self, nums: List[int], target: int) -> int:

        def binary_search(l, r):
            l, r = l, r
            while l <= r: 
                m = (l + r) // 2

                if nums[m] == target:
                    return m 
                
                if nums[m] < target:
                    l = m + 1 
                
                else:
                    r = m - 1
                
            return -1

        l, r, pivot, res = 0, len(nums) - 1, 0, 0

        while l < r: 
            m = (l + r) // 2
            
            if nums[m] < nums[m-1]: 
                pivot = m 
                break

            if nums[m] > nums[-1]:
                l = m + 1

            else:  
                r = m - 1
        
        if l == r: 
            pivot = l

        if target > nums[-1]:
            return binary_search(0, pivot - 1)
        else:
            return binary_search(pivot, len(nums) - 1)