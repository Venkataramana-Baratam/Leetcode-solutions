# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        prev_a = list1
        for _ in range(a-1):
            prev_a = prev_a.next

        next_b = list1
        for _ in range(b+1):
            next_b = next_b.next
        
        temp = list2
        while temp.next:
            temp = temp.next
        prev_a.next = list2
        temp.next = next_b
        return list1