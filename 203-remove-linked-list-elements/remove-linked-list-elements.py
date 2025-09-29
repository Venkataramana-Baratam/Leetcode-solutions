# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        cur = head

        while cur:

            if cur.val != val:
                temp.next = cur
                temp = temp.next
                cur = cur.next
            else:
                cur = cur.next 

        temp.next = None          
        
        return dummy.next