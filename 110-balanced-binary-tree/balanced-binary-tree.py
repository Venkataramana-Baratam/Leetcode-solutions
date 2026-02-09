class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            l = height(node.left)
            r = height(node.right)

            if abs(l - r)>1:
                return -1
            if l==-1 or r==-1:
                return -1
            return 1+max(l,r)
        return height(root)!=-1