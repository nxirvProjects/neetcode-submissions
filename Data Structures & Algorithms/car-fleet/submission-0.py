# (position, speed) then sort it

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = list(zip(position, speed))
        ps.sort()
        stack = []

        for car in reversed(ps):
            time = (target-car[0]) / car[1]
            stack.append(time) # add hours to stack

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)