# put elements that dont have a pair into set
# when finding a pair remove the element-1 out of the set and insert current element
# keep a counter that increments based on every removal

# Return that counter variable


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        streak = 0

        for num in seen:
            if (num -1) not in seen:
                length = 1 # length from the current number
                
                while (num + length) in seen: 
                    length += 1 # increment length up as long as the sequence goes up
                
                streak = max(length, streak)
        
        return streak


            


        return 0

            
