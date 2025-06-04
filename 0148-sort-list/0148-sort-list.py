# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        temp = head
        while temp:
            ans.append(temp.val)
            temp = temp.next
        ans.sort()
        temp = head
        while temp:
            for i in range(len(ans)):
                temp.val = ans[i]
                temp = temp.next
        return head
            