class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxi = 0   

        def height(node):
            if node is None:
                return 0

            lh = height(node.left)
            rh = height(node.right)

            self.maxi = max(self.maxi, lh + rh)

            return 1 + max(lh, rh)

        height(root)
        return self.maxi