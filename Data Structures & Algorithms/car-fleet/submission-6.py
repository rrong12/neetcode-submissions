class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        res = 0
        descend = [(pos, sp) for pos, sp in zip(position, speed)]
        descend.sort(reverse = True)

        for pos, sp in descend:
            stack.append((target - pos) / sp)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)