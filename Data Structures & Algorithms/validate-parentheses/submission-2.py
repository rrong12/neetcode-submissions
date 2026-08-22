class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '{' or c == '(' or c == '[':
                stack.append(c)
            else:
                if not stack: return False 
                last = stack.pop()
                if c == '}' and last != '{': return False
                if c == ')' and last != '(': return False
                if c == ']' and last != '[': return False
        
        if stack: return False
        return True 
