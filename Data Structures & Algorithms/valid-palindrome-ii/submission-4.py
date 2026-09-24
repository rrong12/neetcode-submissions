class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        self.deleted = 0 

        def check(l, r): 
            if l > r: 
                return 

            while l <= r: 
                if s[l] != s[r]: 
                    if self.deleted == 0: 
                        self.deleted = 1
                        return check(l+1, r) or check(l, r-1) 

                    else: 
                        return False
                l += 1 
                r -= 1

            return True 
        return check(l,r)
                
            