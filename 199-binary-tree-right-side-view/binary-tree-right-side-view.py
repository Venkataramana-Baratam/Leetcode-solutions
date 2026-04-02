from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        todo = deque([root])
        res = []

        while todo:
            size = len(todo)

            for i in range(size):
                node = todo.popleft()

                if i == size - 1:  # last node of level
                    res.append(node.val)

                if node.left:
                    todo.append(node.left)
                if node.right:
                    todo.append(node.right)

        return res