# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseAndLength(self, head):
        prev = None
        curr = head
        length = -1

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
            length += 1
        
        return prev, length



    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1.val == 0:
            return l2
        
        if l2.val == 0:
            return l1

        l1, len1 = self.reverseAndLength(l1)
        l2, len2 = self.reverseAndLength(l2)
    
        node1, node2 = l1, l2
        sum1 = sum2 = i = 0 

        while node1 or node2:

            if node1:
                sum1 += node1.val * 10 ** (len1 - i)
                node1 = node1.next
            
            if node2:
                sum2 += node2.val * 10 ** (len2 - i)
                node2 = node2.next
            
            i += 1
        
        total = sum1 + sum2

        resList = curr = ListNode()

        while total > 0:
            curr.next = ListNode(total % 10)
            total //= 10
            curr = curr.next
        
        

        return resList.next