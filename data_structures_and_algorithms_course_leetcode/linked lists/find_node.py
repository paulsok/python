def find_node(head, k):
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow
