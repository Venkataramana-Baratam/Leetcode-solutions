# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        front = head
        while front is not None and front.next is not None:
            slow = slow.next
            front = front.next.next
            if slow==front:
                return True
        return False