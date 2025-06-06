# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        carry = 0
        current = dummy
        while l1 or l2:
            sum = carry
            if l1:
                sum+=l1.val
                l1 = l1.next
            if l2:
                sum+=l2.val
                l2 = l2.next
            carry = sum//10
            current.next = ListNode(sum%10)
            current = current.next
        if carry:
            current.next = ListNode(carry)
        return dummy.next