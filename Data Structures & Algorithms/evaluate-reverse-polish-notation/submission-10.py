class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0 

        for ch in tokens:
            if ch == '+':
                num1 = stack.pop()
                num2 = stack.pop()

                stack.append(int(num2 + num1))
            elif ch == '-':
                num1 = stack.pop()
                num2 = stack.pop()

                stack.append(int(num2 - num1))
            elif ch == '*':
                num1 = stack.pop()
                num2 = stack.pop()

                stack.append(int(num2 * num1))
            elif ch == '/':
                num1 = stack.pop()
                num2 = stack.pop()

                stack.append(int(num2 / num1))
            else:
                stack.append(int(ch))
            
            print(stack)

        
        return stack.pop()





"""
stk = [ 1 2]
stk = [ 3 3 ]
stk = [ 9 4]
stk = 5

return stack.pop
"""

        