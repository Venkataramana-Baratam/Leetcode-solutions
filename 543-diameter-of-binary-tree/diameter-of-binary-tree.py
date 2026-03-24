class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxi = 0
        
        def height(node):
            if node is None:
                return 0
            
            l = height(node.left)
            r = height(node.right)
            
            self.maxi = max(self.maxi, l + r)
            
            return 1 + max(l, r)
        
        height(root)
        return self.maxi