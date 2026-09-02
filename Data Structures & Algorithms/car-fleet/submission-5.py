class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        hashmap = {}
        res = 0
        
        for pos, sp in zip(position, speed):
            hashmap[pos] = sp

        hashmap = dict(sorted(hashmap.items(), reverse = True))

 
        prev_steps = 0 
        for pos, sp in hashmap.items():
            curr_steps = (target - pos) / sp

            if prev_steps == 0:
                prev_steps = curr_steps

            if stack and curr_steps <= prev_steps:
                
                # (4, 1), (2, 3), (0, 2)
                #  6, 8/3, 5 
                stack.pop()
                stack.append((pos, sp, prev_steps))

            else:
                stack.append((pos, sp, curr_steps))
                prev_steps = curr_steps
                res += 1 
    
        print(stack)
        return res