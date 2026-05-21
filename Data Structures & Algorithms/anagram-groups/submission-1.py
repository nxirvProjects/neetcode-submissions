# Uses a default dictionary because we are grouping things together
# sort the letters in the word, and then add any word that has same letter to a list in default dict



from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 
        
        for words in strs:
            letters = list(words)
            letters.sort()

            word2 = "".join(letters) # this is the sorted act word
            res[word2].append(words)
        

        return list(res.values())
        

        