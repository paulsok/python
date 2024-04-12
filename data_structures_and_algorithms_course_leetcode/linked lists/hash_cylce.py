from typing import Optional
from leetcode.linked_list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         seen = set()
#         while head:
#             if head in seen:
#                 return True
#             seen.add(head)
#             head = head.next
#         return False
