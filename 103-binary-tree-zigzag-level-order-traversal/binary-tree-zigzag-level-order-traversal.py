# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        lefttoRight = True
        if root is None:
            return res

        nodesqueue = deque()
        nodesqueue.append(root)

        while nodesqueue:

            size = len(nodesqueue)
            row = [0]*size
            for i in range(size):
                node = nodesqueue.popleft()
                index  = i if lefttoRight else (size - 1 - i)
                row[index] = node.val

                if node.left:
                    nodesqueue.append(node.left)
                if node.right:
                    nodesqueue.append(node.right)
            lefttoRight = not lefttoRight
            res.append(row)
        return res