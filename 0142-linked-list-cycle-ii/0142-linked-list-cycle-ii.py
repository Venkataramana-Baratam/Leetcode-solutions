# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        front = head
        while front is not None and front.next is not None:
            slow =slow.next
            front = front.next.next
            if slow==front:
                slow = head
                while slow!=front:
                    slow = slow.next
                    front = front.next
                return slow
        return None