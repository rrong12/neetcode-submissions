class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def insert_end(self, tail, node):
        node.prev = tail
        tail.next = node
        node.next = None
        return node

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0 
        self.head = self.tail = DoublyNode(-1)
        

    def get(self, key: int) -> int:
        if key in self.cache: #updating the node in the LL 
            curr = self.cache[key]
            if curr.next is not None:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self.tail = self.insert_end(self.tail, curr)
            return curr.val[1]

        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = (key, value)

            if node.next is None:
                return
            node.prev.next = node.next 
            node.next.prev = node.prev 
            self.tail = self.insert_end(self.tail, node)
            return 
            
        self.size += 1
        if self.size > self.capacity:
            node = self.head.next
            if node == self.tail:
                self.tail = self.head
            
            self.head.next = self.head.next.next
            if self.head.next is not None:
                self.head.next.prev = self.head
            self.cache.pop(node.val[0])
            self.size -= 1
        
        self.cache[key] = DoublyNode((key, value), prev=self.tail)
        self.tail.next = self.cache[key]
        self.tail = self.tail.next
        return 