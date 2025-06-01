# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt=0
        temp = head
        temp1 =head
        k=0
        while temp is not None:
            temp=temp.next
            cnt+=1
        if cnt%2!=0:
            k  = math.ceil(cnt/2)
            x = 0
            while temp1 is not None:
                x+=1
                if x==k:
                    return temp1
                temp1 = temp1.next
        else:
            k = math.ceil(cnt/2)
            k+=1
            x = 0
            while temp1 is not None:
                x+=1
                if x==k:
                    return temp1
                temp1 = temp1.next
