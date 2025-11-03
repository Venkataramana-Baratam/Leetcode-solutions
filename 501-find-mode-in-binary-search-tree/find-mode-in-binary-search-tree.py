from collections import Counter

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)

        cnt = Counter(res)
        max_freq = max(cnt.values())
        return [key for key, val in cnt.items() if val == max_freq]
