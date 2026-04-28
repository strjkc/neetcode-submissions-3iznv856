# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_new = ListNode(0)
        c1 = curr_new
        curr_1 = list1
        curr_2 = list2

        while curr_1 and curr_2:
            if curr_1.val <= curr_2.val:
                curr_new.next = curr_1
                curr_1 = curr_1.next
                curr_new = curr_new.next
            else:
                curr_new.next = curr_2
                curr_2 = curr_2.next
                curr_new = curr_new.next
        if curr_1:
            curr_new.next = curr_1
        if curr_2:
            curr_new.next = curr_2
    
        return c1.next

        