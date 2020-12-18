# Linked List

## Linked List Cycle II

+ [Linked List Cycle II](#linked-list-cycle-ii)

https://leetcode.com/problems/linked-list-cycle-ii/

``` python
def detectCycle(self, head: ListNode) -> ListNode:
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
    return None
```