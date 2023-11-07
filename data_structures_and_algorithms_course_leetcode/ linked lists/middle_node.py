from typing import Optional
from leetcode.two_sorted_lists import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next

        for _ in range(length // 2):
            head = head.next

        return head
