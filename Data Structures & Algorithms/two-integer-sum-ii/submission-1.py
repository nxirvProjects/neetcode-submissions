# If sorted, this would mean that if left + right it greater than target to then reduce the right sides index by 1. That way you get a lesser value closer to target. 


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ Time: O(N), Space: O(1)"""
        
        left = 0 
        right = len(numbers)-1

        while left < right:
            if (numbers[left] + numbers[right]) == target:
                return [left+1, right+1]
            elif (numbers[left] + numbers[right]) < target:
                left += 1
            elif (numbers[left] + numbers[right]) > target: 
                right -= 1
        




