class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok == '+': 
                n1, n2 = self.getOp(stack)
                stack.append(n1 + n2)
            elif tok == '-':
                n1, n2 = self.getOp(stack)
                stack.append(n2 - n1)
            elif tok == '*':
                n1, n2 = self.getOp(stack)
                stack.append(n1 * n2)
            elif tok == '/':
                n1, n2 = self.getOp(stack)
                stack.append(int(n2 / n1))
            else: stack.append(int(tok))

        return stack[0]

    def getOp(self, stack) -> tuple[int,int]:
        op1 = stack.pop()
        op2 = stack.pop()
        return op1, op2
