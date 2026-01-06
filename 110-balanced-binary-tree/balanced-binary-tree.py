# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            l = height(node.left)
            r = height(node.right)
            return 1 + max(l,r)        
        if root is None:
            return True
        left = height(root.left)
        right = height(root.right)
        if abs(left - right)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
