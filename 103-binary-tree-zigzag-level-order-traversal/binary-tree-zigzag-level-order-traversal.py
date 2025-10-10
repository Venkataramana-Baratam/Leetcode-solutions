# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        nodesqueue = deque()
        nodesqueue.append(root)
        leftToright = True
        while nodesqueue:
            size = len(nodesqueue)
            row = [0]*size
            for i in range(size):

                node = nodesqueue.popleft()
                index = i if leftToright else (size-1-i)

                row[index] = node.val
                if node.left:
                    nodesqueue.append(node.left)
                if node.right:
                    nodesqueue.append(node.right)
            leftToright = not leftToright
            result.append(row)
        return result