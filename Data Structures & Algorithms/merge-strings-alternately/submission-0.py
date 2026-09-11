class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l = 0 
        res = ""

        while l < len(word1) and l < len(word2):
            res = res + word1[l] + word2[l]
            l += 1
        
        if l == len(word1):
            res += word2[l:]
        
        else:
            res += word1[l:]
        
        return res



        