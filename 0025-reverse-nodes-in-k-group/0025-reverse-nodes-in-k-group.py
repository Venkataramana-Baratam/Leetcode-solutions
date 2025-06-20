# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            temp = head
            prev = None
            while temp is not None:
                front  = temp.next
                temp.next = prev
                prev = temp 
                temp = front
            return prev
        def findkthnode(temp,k):
            k-=1
            while temp is not None and k>0:
                temp = temp.next
                k-=1
            return temp
        temp = head
        prevnode = None
        nextnode = None
        while temp is not None:
            kthnode = findkthnode(temp,k)
            if kthnode is None:
                if prevnode:
                    prevnode.next = temp
                break
            nextnode = kthnode.next
            kthnode.next = None
            reverse(temp)
            if temp == head:
                head = kthnode
            else:
                prevnode.next =  kthnode
            prevnode = temp
            temp = nextnode
        return head
