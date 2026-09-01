class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [-1] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                val, ind = stack.pop()
                res[ind] = i - ind
            
            stack.append((t, i))
        


        while stack:
            val, ind = stack.pop()
            res[ind] = 0
        
        return res
