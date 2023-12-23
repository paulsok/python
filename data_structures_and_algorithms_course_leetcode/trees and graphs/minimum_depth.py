from typing import Optional
from practicum.tree_node import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if left == 0:
                return right + 1
            if right == 0:
                return left + 1

            return min(left,right) + 1
        return dfs(root)
