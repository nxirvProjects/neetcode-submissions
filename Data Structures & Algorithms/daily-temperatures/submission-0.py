class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stk = []

        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]: # while stk is not empty and current index value is greater then whats in stk
                idx = stk.pop()
                result[idx] = i-idx
            stk.append(i)
        
        return result