class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        left = 1 
        right = len(nums)-1
        N = len(nums)-1

        nums.sort()
        result = []


        for i in range(0, N):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            left = i+1
            right = len(nums)-1

            while left < right:
                target = nums[i] + nums[left] + nums[right]

                if target == 0: 
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    
                elif target > 0: 
                    right -= 1
                else: 
                    left += 1
                
                
        
        return result





