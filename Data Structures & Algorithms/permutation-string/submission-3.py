class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False 

        freq1 = [0] * 26
        for s in s1: 
            freq1[ord(s) - ord('a')] += 1
    
        l, r = 0, 0
        freq2 = [0] * 26
        for i in range(len(s1) - 1):
            freq2[ord(s2[i]) - ord('a')] += 1

        for r in range(len(s1) - 1, len(s2)):
            freq2[ord(s2[r]) - ord('a')] += 1
            
            if freq2 == freq1:
                return True
            
            freq2[ord(s2[l]) - ord('a')] -= 1
            l += 1

        return False