class Node:
    def __init__(self, key, val, next = None):
        self.val = (key, val)
        self.next = next


class MyHashMap:

    def __init__(self):
        self.buckets = [None] * 5000

    def hash(self, key: int) -> int:
        return key % 5000
        
    def put(self, key: int, value: int) -> None:
        hash_val = self.hash(key)
        if not self.buckets[hash_val]:
            self.buckets[hash_val] = Node(key, value)
        else:
            curr = self.buckets[hash_val]
            while True:
                if curr.val[0] == key: 
                    curr.val = (key, value)
                    return
                if not curr.next: break
                curr = curr.next 
            
            curr.next = Node(key, value)
        

    def get(self, key: int) -> int:
        hash_val = self.hash(key)
        if not self.buckets[hash_val]: return -1 
        curr = self.buckets[hash_val]

        while curr:
            if curr.val[0] == key: 
                return curr.val[1]
            curr = curr.next
        
        return -1 
        

    def remove(self, key: int) -> None:
        if self.get(key) == -1: return

        hash_val = self.hash(key)
        curr = self.buckets[hash_val]

        if curr.val[0] == key: 
            self.buckets[hash_val] = curr.next
            return
        
        while curr.next:
            if curr.next.val[0] == key:
                curr.next = curr.next.next
                return
            curr = curr.next
            
        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)