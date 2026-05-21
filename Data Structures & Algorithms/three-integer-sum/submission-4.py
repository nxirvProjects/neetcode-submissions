class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        l = i+1
        r = len(nums)-1
        res = []

        nums.sort()

        for i in range(len(nums)-1):
            # to skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1

            while l < r: 
                total = (nums[i] + nums[l] + nums[r])

       
                
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    # Skip the duplicates for left pointer 
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif total < 0:
                    l += 1
                else: 
                    r -= 1

        return res