class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        leftMax, rightMax = 0, 0
        total = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if height[left] <= height[right]: 
                total += max(0, leftMax - height[left])
                left += 1
            else: 
                total += max(0, rightMax - height[right])
                right -= 1
        
        return total

