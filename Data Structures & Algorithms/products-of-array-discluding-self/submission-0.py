class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        pre = [0] * N  
        post = [0] * N
        res = [0] * N

        pre[0] = 1
        post[N-1] = 1


        for i in range(N-1):
            pre[i+1] = pre[i] * nums[i] # populate the prefixes
        
        for i in reversed(range(1, N)):
            post[i-1] = post[i] * nums[i]
            
        
        for i in range(N):
            res[i] = pre[i] * post[i]
        
        return res