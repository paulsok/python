from typing import Optional

from practicum.tree_node import TreeNode


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        while root:
            ans = min(root.val, ans, key = lambda x: (abs(target - x), x))
            root = root.left if target < root.val else root.right
        return ans
