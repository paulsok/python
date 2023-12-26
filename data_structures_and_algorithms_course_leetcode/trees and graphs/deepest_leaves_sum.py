from collections import deque
from typing import Optional

from practicum.tree_node import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        while queue:
            current_level = queue
            queue = deque()

            for node in current_level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return sum(node.val for node in current_level)
