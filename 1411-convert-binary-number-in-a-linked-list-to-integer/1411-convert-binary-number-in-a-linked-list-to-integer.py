# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = []
        temp = head
        p2 =1
        while temp:
            ans.append(temp.val)
            temp = temp.next
        n = len(ans)
        num=0
        for i in range(n-1,-1,-1):
            if ans[i]==1:
                num = num+p2
            p2 =p2*2
        return num