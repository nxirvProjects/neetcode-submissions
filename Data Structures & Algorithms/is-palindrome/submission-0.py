# Since we are technically finding a matching pair from both sides. We should use two pointers converging

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Remember to create new string since strings are immutable in python, meaning the original string cannot be changed
        s = s.lower()
        newString = re.sub(r'[^a-zA-Z0-9]', '', s)
        

        
        left = 0
        right = len(newString)-1

        while left < right:
            print(newString[left], newString[right])

            if newString[left] != newString[right]: 
                return False
            
            left += 1
            right -= 1

        return True
        