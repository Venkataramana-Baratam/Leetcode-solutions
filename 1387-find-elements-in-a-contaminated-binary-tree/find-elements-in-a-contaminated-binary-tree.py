# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val=0
        self.traverse(1,root.left)
        self.traverse(2,root.right)
        self.root=root

    def traverse(self,val,node):
        if node is None:
            return

        node.val=val
        self.traverse(2*val+1,node.left)
        self.traverse(2*val+2,node.right) 

    def find(self, target: int) -> bool:
        return self.pot(target,self.root)

    def pot(self,target,node):
        if node is None:
            return False

        if node.val==target:
            return True
        return self.pot(target,node.left) or self.pot(target,node.right)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)