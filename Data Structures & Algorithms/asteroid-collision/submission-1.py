class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if not stack or stack[-1] < 0:
                stack.append(ast)

            else:
                if ast > 0:
                    stack.append(ast)
                else:
                    if abs(ast) > stack[-1]:
                        while stack and stack[-1] > 0 and abs(ast) > stack[-1]:
                            stack.pop()
                        if not stack or stack[-1] < 0:
                            stack.append(ast)

                    if abs(ast) == stack[-1]:
                        stack.pop()
                        continue

                    elif abs(ast) > stack[-1]:
                        continue

        return stack
