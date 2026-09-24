class PrefixTree:

    def __init__(self):
        self.trie = [[0] * 26]
        self.length = 0
        self.hashset = set()

    def insert(self, word: str) -> None: #O(n)
        i = 0 
        for c in word: 
            if self.trie[i][ord(c) - ord('a')] == 0: 
                self.length += 1
                self.trie.append([0] * 26)
                self.trie[i][ord(c) - ord('a')] = self.length
                i = self.length
            else: 
                i = self.trie[i][ord(c) - ord('a')]


        self.hashset.add(word)

    def search(self, word: str) -> bool:
        return word in self.hashset

    def startsWith(self, prefix: str) -> bool: 
        i = 0 
        for c in prefix: 
            if self.trie[i][ord(c) - ord('a')] == 0: 
                return False
            i = self.trie[i][ord(c) - ord('a')]
        
        return True 
        
        