# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        res = []

        nodesqueue = deque()
        nodesqueue.append(root)
        lefttoright = True
        if root is None:
            return res
        while nodesqueue:
            size = len(nodesqueue)
            row = [0] *size
            for i in range(len(row)):
                node = nodesqueue.popleft()
                index = i if lefttoright else (size - i - 1)
                
                row[index] = node.val

                if node.left:

                    nodesqueue.append(node.left)
                if node.right:
                    nodesqueue.append(node.right)
            lefttoright = not lefttoright
            res.append(row)

        return res