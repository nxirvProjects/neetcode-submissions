# output is a list of indicies
# target - num in nums = other number

# dict which contains prev values
# target - prev ? current value
# if true return current val index and prev index in a list format

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      prevMap = {}

      for i, num in enumerate(nums):
        diff = target - num

        if diff in prevMap:
            return [prevMap[diff], i]
        
        prevMap[num] = i

