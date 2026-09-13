# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2: 
            return None
        l1, l2 = list1, list2
        head = ListNode(101)
        l3 = head
    
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    l3.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    l3.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next

        return head.next