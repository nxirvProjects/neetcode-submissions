# i j and k have to be unique indicies. 
# cannot have duplicate triplets. 
# Space is O(1) and time is O(n^2)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for loop to set intial index i, 
        # And then a nested while loop to squeeze indicies j and k

        res = []
        nums.sort()

        for i in range(0, len(nums)-1):
            left = i+1
            right = len(nums)-1

            # If the starting i value is greater than 0 and the array is sorted this means you will never find a triplet
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right: 
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif nums[i] + nums[left] + nums[right] < 0: 
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                     right -= 1
         

        return res





