# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        
        res = 0
        def inorder(node):
            nonlocal res
            if node is None:
                return 
            inorder(node.left)
            if low<=node.val<=high:
                res+=node.val
            inorder(node.right)
        inorder(root)
        return res