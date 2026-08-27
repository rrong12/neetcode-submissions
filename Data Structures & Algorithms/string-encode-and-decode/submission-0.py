class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res += (str(len(s)) + '#' + s)

        print(res)
        return res
       
    def decode(self, s: str) -> List[str]:

        res = []
        counter = 0 
        n = len(s)
        i = 0 
        while i < n:
            if s[i] == '#':
                length = int(s[i-counter: i])
                res.append(s[i+1: i+1+length]) 
                i += length
                counter = -1
            
            counter += 1
            i += 1

        return res



        
