from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majC = Counter(nums)

        max_key = max(majC, key=majC.get)

        return max_key  