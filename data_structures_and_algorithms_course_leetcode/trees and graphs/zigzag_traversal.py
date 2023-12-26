from collections import deque
from typing import List, Optional
from practicum.tree_node import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = [[root.val]]
        queue = deque([root])
        counter = 2

        while queue:
            current_length = len(queue)

            for _ in range(current_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if  counter % 2 and queue:
                ans.append([node.val for node in queue])
            elif not counter % 2 and queue:
                ans.append([node.val for node in queue][::-1])
            counter +=1

        return ans
