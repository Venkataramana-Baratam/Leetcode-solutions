# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 1
        temp1 = head
        while temp1.next is not None:
            cnt += 1
            temp1 = temp1.next

        def delete_from_pos(head):
            if head is None:
                return head
            pos = cnt - n + 1
            if pos == 1:
                temp = head
                head = head.next
                del temp
                return head
            else:
                temp = head
                i = 1
                while i < pos - 1 and temp.next is not None:
                    temp = temp.next
                    i += 1
                if temp.next is None:
                    return head
                next_node = temp.next
                temp.next = next_node.next
                del next_node
                return head

        return delete_from_pos(head)
