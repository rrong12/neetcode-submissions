import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = "".join(ch for ch in s if ch in string.ascii_letters + string.digits)
        

        l, r = 0, len(cleaned) - 1
        while l < r: 
            if cleaned[l] != cleaned[r]:
                return False
            l += 1
            r -= 1

        return True 