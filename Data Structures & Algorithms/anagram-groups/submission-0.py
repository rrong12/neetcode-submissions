class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_strs = []
        hashmap = {}

        for i in range(len(strs)):
            sorted_val = "".join(sorted(strs[i]))
            if sorted_val in hashmap:
                hashmap[sorted_val].append(i)
            else:
                hashmap[sorted_val] = [i]

        res = []

        for r in hashmap.values():
            res.append([strs[i] for i in r])
        
        return res