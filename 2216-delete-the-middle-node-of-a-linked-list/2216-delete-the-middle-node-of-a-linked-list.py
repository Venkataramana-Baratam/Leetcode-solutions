# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = head
        front = head
        prev = slow
        while front and front.next and slow:
            prev = slow
            slow = slow.next
            front = front.next.next
        prev.next = slow.next
        del slow
        return head