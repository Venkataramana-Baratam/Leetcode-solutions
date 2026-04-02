# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ds = []

        if root is None:
            return []
        def f(node,val):

            if node is None:
                return None

            if val==len(ds):
                ds.append(node.val)

            f(node.right,val+1)
            f(node.left,val+1)

            return ds

        res = f(root,0)
        return res