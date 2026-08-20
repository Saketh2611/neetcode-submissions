class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch not in ['+', '-', '*', '/']:
                stack.append(int(ch))
            else:
                n1 = stack.pop()
                n2 = stack.pop()

                if ch == '+':
                    stack.append(n2 + n1)
                elif ch == '-':
                    stack.append(n2 - n1)
                elif ch == '*':
                    stack.append(n2 * n1)
                else:  # '/'
                    stack.append(int(n2 / n1))  # truncate toward zero

        return stack[0]
