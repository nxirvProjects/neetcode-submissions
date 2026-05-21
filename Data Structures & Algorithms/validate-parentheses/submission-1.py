# stack would be a list


class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {
            '}': '{',
            ']': '[',
            ')': '('
        } 

        for symbol in s:
            if symbol in ')]}':
                if not stk or stk[-1] != pairs[symbol]: 
                    return False
                stk.pop()
            elif symbol in '{[(':
                stk.append(symbol)
        
        return len(stk) == 0

