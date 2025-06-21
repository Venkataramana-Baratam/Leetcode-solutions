# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        n = 0
        temp = head
        while temp:
            temp = temp.next
            n+=1
        k  = k%n
        if k==0:
            return head
        i = n - k
        temp1 = head
        for _ in range(i-1):
            temp1 = temp1.next
        new_head = temp1.next
        nextnode = new_head
        temp1.next = None
        while nextnode.next:
            nextnode = nextnode.next
        nextnode.next = head
        return new_head
