from typing import Optional

from practicum.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, small, large):
            if not node:
                return True
            
            if not (small < node.val < large):
                return False

            left = dfs(node.left, small, node.val)
            right = dfs(node.right, node.val, large)

            # tree is a BST if left and right subtrees are also BSTs
            return left and right

        return dfs(root, float("-inf"), float("inf"))
