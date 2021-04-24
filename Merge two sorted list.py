# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        tail = l3 = ListNode()
        
        while(1):
            if(l1 is None):
                tail.next = l2
                break
            if(l2 is None):
                tail.next = l1
                break
            if(l1.val <= l2.val):
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next  
            
            tail = tail.next
            
        
        return l3.next