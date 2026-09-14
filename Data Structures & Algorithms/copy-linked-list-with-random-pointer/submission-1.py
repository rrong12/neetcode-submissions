"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None 
        nodeMap = {}
        newHead = Node(head.val)
        nodeMap[head] = newHead
        curr1 = head.next
        curr2 = newHead
        
        while curr1: 
            curr2.next = Node(curr1.val)
            nodeMap[curr1] = curr2.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        curr2.next = None

        curr1, curr2 = head, newHead

        while curr1:
            if not curr1.random:
                curr2.random = None
            else:
                curr2.random = nodeMap[curr1.random]
            
            curr1 = curr1.next
            curr2 = curr2.next
        
        return newHead




