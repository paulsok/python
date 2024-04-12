from typing import Optional
from leetcode.linked_list import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            if curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
