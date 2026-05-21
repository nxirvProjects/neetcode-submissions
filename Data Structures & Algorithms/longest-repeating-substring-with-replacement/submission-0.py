class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      l = 0
      count = {} 
      res = 0
      
      for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0) 
        windowL = (r-l) + 1
        maxC = max(count.values()) # 26 diffent letters 


        if windowL-maxC <= k:
            r += 1
            res = max(res, windowL)
        else:
            count[s[l]] -= 1
            l += 1
            
      return res

        
        