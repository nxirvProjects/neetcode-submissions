# Return k most freq numbers in list
# I need to count occurence of numbers, Not using counter but a regular dict

from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1: 1, 2: 2, 3: 3
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1

        result = heapq.nlargest(k, count.keys(), key = count.get) 

        return result


            
