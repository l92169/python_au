# Intervals

+ [Reverse Linked List](#reverse-linked-list)

##Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

``` python
def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    next = None
    cur = head
    while cur != None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return  prev
```
