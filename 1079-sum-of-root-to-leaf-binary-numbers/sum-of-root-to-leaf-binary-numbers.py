# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        

        def fun(node,path):

            if node is None:
                return 0

            path = path + str(node.val)

            if node.left is None and node.right is None:
                return int(path,2)

            return fun(node.left,path) + fun(node.right,path)

        return fun(root,"")