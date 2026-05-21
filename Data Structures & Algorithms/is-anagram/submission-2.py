from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = Counter(s)

        for letter in t:
            if letter in sCount:
                sCount[letter] -= 1
            
            if sCount[letter] == 0: 
                del sCount[letter]

        
        if not sCount: 
            return True
        

        return False

        