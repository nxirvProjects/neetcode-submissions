from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs: 
            letters = list(word)
            letters.sort() # sort the letters for hashmap

            anagram = "".join(letters)
            anagrams[anagram].append(word)
        
        return list(anagrams.values())

