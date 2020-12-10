# Linked List

## Linked List Cycle

+ [Linked List Cycle](#linked-list-cycle)

https://leetcode.com/problems/linked-list-cycle/

``` python
def hasCycle(self, head: ListNode) -> bool:
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False
```