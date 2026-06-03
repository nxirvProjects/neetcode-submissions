import math

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        res = 0

        while left <= right: 
            mid = (left+right) // 2

            if (mid * mid) < x:
                left = mid+1
                res = mid
            elif (mid * mid) > x:
                right = mid-1
            else:
                return mid # mid == x thats the target

        return res