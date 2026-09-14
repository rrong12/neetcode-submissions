# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head 

        while head.next and head.next.next: #might not work for even case? 

            while curr.next.next:
                curr = curr.next
            
            temp = head.next
            head.next = curr.next
            curr.next.next = temp
            curr.next = None 
            
            head = head.next.next
            curr = head

        return



