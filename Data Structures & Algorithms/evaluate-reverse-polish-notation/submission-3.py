class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = list()
        operators = ['+', '-', '*', '/']
        for i in tokens:
            if i in operators:
                second = stack.pop()
                first = stack.pop()
                if i == '+':
                    stack.append(first + second)
                if i == '-':
                    stack.append(first - second)
                if i == '*':
                    stack.append(first * second)
                if i == '/':
                    stack.append(int(first / second))
            else:
                stack.append(int(i))
        return stack.pop()