class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        # 1 2 3 3

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
            
        
        return False
        
