# Container calculated via length * width = Area
# key is that we care about a greater amount of width opposed to height

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # distance between the points
        # min height between the two points
        # max between greatest output

        left = 0 
        right = len(heights)-1
        res = 0

        while left < right: 
            dist = right-left

            minPoint = min(heights[left], heights[right])
            area = minPoint * dist

            res = max(res, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res





        